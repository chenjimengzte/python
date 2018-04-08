from PIL import Image, ImageFilter

im = Image.open('a.jpg')

#模糊滤镜

im2 = im.filter(ImageFilter.BLUR)

im2.save('a_filter.jpg' , 'jpeg')
