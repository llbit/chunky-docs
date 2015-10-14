from PIL import Image
from PIL import ImageOps
import os, sys

if len(sys.argv) is not 3:
    print('Usage: thumbnail.py [input] [output]')
    sys.exit(1)

input = sys.argv[1]
output = sys.argv[2]
try:
	img = Image.open(input)
	img = ImageOps.fit(img, (256, 256), Image.ANTIALIAS)
	img.save(output, 'JPEG')
except IOError as e:
	print("failed to create thumbnail of %s" % input)
	print(e)
