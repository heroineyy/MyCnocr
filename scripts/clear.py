from PIL import Image, ImageFilter

# 打开图像
im = Image.open(r"E:\dataset\PNGImages_OCR\C46188_2.png")

# 应用锐化滤镜
im_sharp = im.filter(ImageFilter.SHARPEN)

# 保存图像
im_sharp.save(r"E:\dataset\PNGImages_OCR\image_sharpened.jpg")