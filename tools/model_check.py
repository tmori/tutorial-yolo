from ultralytics import YOLO
from torchinfo import summary

# 学習済みモデルをロード
#model = YOLO("runs/detect/train/weights/best.pt")
model = YOLO("yolov8n.pt") 

# クラス数とクラス名を表示
print("学習済みモデルのクラス一覧:", model.names)
print("クラス数:", len(model.names))


# モデルの概要を表示（深さを確認）
summary(model.model, input_size=(1, 3, 640, 640), depth=5)

# 全レイヤーを一覧表示
for i, layer in enumerate(model.model.children()):
    print(f"Layer {i}: {layer}")