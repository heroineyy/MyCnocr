from PIL import Image
import os

# 设置要处理的文件夹路径
folder_path = '/path/to/folder'

# 设置要缩放的倍数
scale_factor = 0.5

# 遍历文件夹下的所有图片文件
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 打开图片
        img = Image.open(os.path.join(folder_path, filename))

        # 计算缩放后的大小
        width, height = img.size
        new_width, new_height = int(width * scale_factor), int(height * scale_factor)

        # 缩放图片
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # 保存缩放后的图片
        img.save(os.path.join(folder_path, f'scaled_{scale_factor}x_{filename}'))
