# epicflow-python2/3

Abstract Epicflow with python2/3

## 1. Compile

*   compile SED_edge

```
$ cd ./lib/SED_edge
$ mex private/edgesDetectMex.cpp -outdir private
$ mex private/edgesNmsMex.cpp    -outdir private
$ mex private/spDetectMex.cpp    -outdir private
$ mex private/edgeBoxesMex.cpp   -outdir private
```

*   compile flow-code

```
$ cd ./lib/flow-code
$ cd imageLib
$ make
$ cd ..
$ make
```

## 2. Run example

```
$ python3 example.py
```

## 3. Interface

more information reference file 'example.py' please.

And in `abstract_epic.py` file, we show how to abstract the feature in `i-LIDS-VID` dataset.
