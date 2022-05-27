from PIL import Image, ImageFilter

before = Image.open("yard.bmp")
after = before.filter(ImageFilte
# 10 pixels at a timer.BoxBlur(10))

after.save("out.bmp")