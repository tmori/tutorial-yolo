from PIL import Image
import os

# 新しい幅
new_width = 640
dir_path = './datasets-drone/images/train'

# カレントディレクトリ内のすべてのファイル
for filename in os.listdir(dir_path):
    # .jpgファイルのみを処理
    if filename.endswith('.png'):
        print(f"{filename} を変換")
        filepath = dir_path + '/' + filename
        with Image.open(filepath) as img:
            # アスペクト比を保持した高さを計算
            aspect_ratio = new_width / img.width
            new_height = int(img.height * aspect_ratio)
            # リサイズ
            resized_img = img.resize((new_width, new_height))
            # 元のファイルを上書き
            resized_img.save(filepath)

exit()
