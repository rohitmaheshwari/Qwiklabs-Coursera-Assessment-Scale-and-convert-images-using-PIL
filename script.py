#T7usr/bin/python3

from PIL import Image
import os, glob

path = 'images'
output_path = '/opt/icons'

for filename in glob.glob(os.path.join(path, '*')):
        with Image.open(filename) as im:
                  im = im.convert('RGB')
                  im.rotate(-90).resize((128, 128)).save(output_path + filename.split('images')[1], 'jpeg')
