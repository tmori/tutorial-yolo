#!/bin/bash

if [ $# -ne 2 ]
then
    echo "Usage: $0 <path_to_json_dir> <path_to_out_dir>"
    exit 1
fi

PATH_TO_JSON_DIR=${1}
PATH_TO_OUT_DIR=`pwd`/${2}

# Convert json to yolo format
labelme2yolo -d ${PATH_TO_JSON_DIR}

# Move yolo files to out dir
mv ${PATH_TO_JSON_DIR}/YOLODataset ${PATH_TO_OUT_DIR}

# by using yq, the path in dataset.yaml changes to PATH_TOU_OUT_DIR
yq eval ".path = \"${PATH_TO_OUT_DIR}/YOLODataset\"" -i "${PATH_TO_OUT_DIR}/YOLODataset/dataset.yaml"

echo "Updated dataset.yaml with new path: ${PATH_TO_OUT_DIR}/YOLODataset"

