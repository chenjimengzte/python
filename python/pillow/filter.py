from PIL import Image

im = Image.open('a.jpg')

w,h = im.size

print('image size : %s x %s' % (w,h))

#缩放

im.thumbnail((w//2, h//2))

print('Resize image to : %s x %s' % (w//2,h//2))

im.save('a_thumbnail.jpg' , 'jpeg')

