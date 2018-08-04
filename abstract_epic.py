import os
import argparse
from lib import get_epicflow

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--rgb_root', type=str, default='/home/yonghui/Documents/i-LIDS-VID/sequences')
parser.add_argument('--flow_root', type=str, default='/home/yonghui/Documents/i-LIDS-VID-EpicFlow/sequences')
args = parser.parse_args()

rgb_root = args.rgb_root
flow_root = args.flow_root

task_list = []

cam_list = os.listdir(rgb_root)

for cam_id in cam_list:
    rgb_cam = os.path.join(rgb_root, cam_id)
    flow_cam = os.path.join(flow_root, cam_id)

    person_list = os.listdir(rgb_cam)
    for person_id in person_list:
        rgb_person = os.path.join(rgb_cam, person_id)
        flow_person = os.path.join(flow_cam, person_id)

        if os.path.isdir(flow_person) is False:
            os.makedirs(flow_person)

        img_list = os.listdir(rgb_person)
        img_list = sorted(os.listdir(rgb_person), key=lambda x: int(x[-9:-4]))
        for i in range(len(img_list) - 1):
            img1_path = os.path.join(rgb_person, img_list[i])
            img2_path = os.path.join(rgb_person, img_list[i + 1])
            out_path = os.path.join(flow_person, img_list[i])
            task_list.append([img1_path, img2_path, out_path])


get_epicflow(task_list=task_list, thread_num=35, lib_path='./lib')
