# Example file for Python Essential Libraries course by Joe Marini
# demonstrates simple image operations using the Pillow library
from PIL import Image

# TODO: read an image and examine some basic attributes using the Image class
image = Image.open('Exercise Files/Pillow/ImagesArchive/Data.jpeg')
# print(image.filename)
# print(image.format)
# print(image.size)
# print(image.height)
# print(image.width)
# print(image.mode)
# for k, v in image.info.items():
#     print('Key: {0}, value: {1}'.format(k,v))

# TODO: use the save function to convert an image to a new type
# outfile = 'Exercise Files/Pillow/ImagesArchive/Data.png'
# image.save(outfile, 'PNG')
# with Image.open(outfile) as im:
#     print('Image format:', im.format)

# TODO: show the image using the platform viewer app
image.show()
