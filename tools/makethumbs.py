from PIL import Image
from PIL import ImageOps
import os, sys

for name in os.listdir('images/gallery'):
	try:
		out = name[:-4] + "_thumb.jpg"
		img = Image.open(os.path.join('images/gallery/', name))
		img = ImageOps.fit(img, (256, 256), Image.ANTIALIAS)
		img.save(os.path.join('out/gallery/', out), 'JPEG')
	except IOError as e:
		print "failed to create thumbnail"
		print e
