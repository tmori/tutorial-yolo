#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Usage: $0 <train_num> <path_to_image_file>"
    exit 1
fi

BEST_PT=./runs/detect/train${1}/weights/best.pt
IMAGE_FILE=$2

if [ ! -f ${BEST_PT} ]
then
    echo "Model not found: ${BEST_PT}"
    exit 1
fi

if [ ! -f ${IMAGE_FILE} ]
then
    echo "Image file not found: ${IMAGE_FILE}"
    exit 1
fi

 yolo task=detect mode=predict \
    model=${BEST_PT} source=${IMAGE_FILE}