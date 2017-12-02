import os
import threading
import time

lock = threading.RLock()

task_idx = 0
task_tot = 0
task_list = []
lib_path = ""


def transtoflo(thread_name):
    global task_idx
    trans_cmd = 'cd {}; matlab -nodisplay -r \"'.format(lib_path)
    while True:
        lock.acquire()
        if task_idx >= task_tot:
            lock.release()
            break
        img1_path, img2_path, out_path = task_list[task_idx]
        task_idx += 1
        lock.release()
        trans_cmd += 'get_epicflow(\'{}\', \'{}\', \'{}.flo\'); '.format(img1_path, img2_path, out_path[:-4])
    trans_cmd += 'exit;\"'
    # print('trans_cmd=', trans_cmd)
    os.system(trans_cmd)


def transtopng(thread_name):
    global task_idx
    while True:
        lock.acquire()
        if task_idx >= task_tot:
            lock.release()
            break
        _, _, out_path = task_list[task_idx]
        task_idx += 1
        lock.release()

        transcmd = 'cd {}; flow-code/color_flow {}.flo {}'.format(lib_path, out_path[:-4], out_path)
        os.system(transcmd)
        delcmd = 'cd {}; rm {}.flo'.format(lib_path, out_path[:-4])
        os.system(delcmd)


def get_epicflow(**args):
    '''
    task_list=[]
    thread_num = 5
    lib_path = ./lib
    '''
    global task_list
    global task_tot
    global lib_path
    global task_idx

    task_list = args['task_list']
    task_tot = len(task_list)
    lib_path = args['lib_path']

    thread_num = args['thread_num']

    task_idx = 0
    transtoflo_list = []
    for thread_name in range(thread_num):
        transtoflo_list.append(threading.Thread(target=transtoflo, args=(thread_name,)))
        transtoflo_list[-1].start()
    for thread in transtoflo_list:
        thread.join()

    print('################## flo->png ##################')

    task_idx = 0
    transtopng_list = []
    for thread_name in range(thread_num):
        transtopng_list.append(threading.Thread(target=transtopng, args=(thread_name,)))
        transtopng_list[-1].start()
    for thread in transtopng_list:
        thread.join()

