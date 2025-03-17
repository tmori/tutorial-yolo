#!/bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 <epoch_num>"
    exit 1
fi

DATA_SET_PATH=`pwd`/YOLODataset/dataset.yaml
EPOCH_NUM=$1
IMGSIZE=640

yolo task=detect mode=train model=yolov8n.pt \
    data=${DATA_SET_PATH} \
    epochs=${EPOCH_NUM} \
    imgsz=${IMGSIZE} 
