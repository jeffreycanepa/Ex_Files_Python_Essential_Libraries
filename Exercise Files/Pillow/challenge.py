'''Get all the images in a directory and make a thumbnail file'''

from PIL import Image
import glob
import os

thumbsize = (128, 128)
myDir = 'Exercise Files/Pillow/ImagesArchive/'
images = glob.glob(myDir + '*.*')

for image in images:
   if image.endswith('.jpeg') or image.endswith('.png') or image.endswith('.gif'):
      fn = os.path.basename(image)
      filename, ext = os.path.splitext(fn)
      with Image.open(image) as imgfile:
        imgfile.thumbnail(thumbsize)
        imgfile.save(myDir + filename + ".thumb" + ext)
