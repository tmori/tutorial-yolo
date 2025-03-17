import sys
import json
from ultralytics import YOLO

def detect_objects(model_path, image_path):
    # YOLO モデルをロード
    model = YOLO(model_path)

    # 画像を推論
    results = model(image_path) 

    # 検出結果を JSON に変換
    detections = []
    for result in results:
        for box in result.boxes.data:
            x1, y1, x2, y2, conf, cls = box.tolist()
            detections.append({
                "object": result.names[int(cls)],  # クラス名（例: "drone"）
                "confidence": round(conf, 2),  # 確信度
                "bounding_box": {
                    "x_min": int(x1),
                    "y_min": int(y1),
                    "x_max": int(x2),
                    "y_max": int(y2)
                }
            })

    # JSON 出力
    json_data = json.dumps(detections, indent=4)
    print(json_data)

    # JSON をファイルに保存
    with open("detections.json", "w") as f:
        f.write(json_data)


if __name__ == "__main__":
    # 引数の処理
    if len(sys.argv) != 3:
        print("USAGE: python script.py <model_path> <image_path>")
        sys.exit(1)
    
    model_path = sys.argv[1]
    image_path = sys.argv[2]
    detect_objects(model_path, image_path)
