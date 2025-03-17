#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 <epoch_num>"
    exit 1
fi

DATA_SET_PATH=`pwd`/YOLODataset/dataset.yaml
EPOCH_NUM=$1
IMGSIZE=640

yolo task=detect mode=train model=yolov8x.pt \
    workers=4 \
    batch=8 \
    pretrained=True \
    data=${DATA_SET_PATH} \
    epochs=${EPOCH_NUM} \
    imgsz=${IMGSIZE} \
    device=mps \
    freeze=22

#    cache=True \
#    freeze=22


