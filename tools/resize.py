import os
import sys
from PIL import Image

def resize_images(dir_path, new_width=640):
    """
    指定したディレクトリ内のPNG画像をリサイズする。
    - アスペクト比を保持
    - 幅を new_width に変更（デフォルトは 640）
    """
    if not os.path.exists(dir_path):
        print(f"エラー: 指定したディレクトリが存在しません: {dir_path}")
        return
    
    # ディレクトリ内のファイルを処理
    for filename in os.listdir(dir_path):
        if filename.endswith('.png'):
            filepath = os.path.join(dir_path, filename)
            print(f"{filename} を変換中...")
            with Image.open(filepath) as img:
                aspect_ratio = new_width / img.width
                new_height = int(img.height * aspect_ratio)
                resized_img = img.resize((new_width, new_height))
                resized_img.save(filepath)  # 上書き保存

    print("✅ 画像のリサイズ完了！")

if __name__ == "__main__":
    # 引数の処理
    if len(sys.argv) < 2:
        print("使い方: python script.py <ディレクトリパス> [リサイズ後の幅 (デフォルト640)]")
        sys.exit(1)
    
    dir_path = sys.argv[1]
    new_width = int(sys.argv[2]) if len(sys.argv) > 2 else 640

    resize_images(dir_path, new_width)
