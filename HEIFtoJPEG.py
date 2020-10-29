from PIL import Image
import os
import pyheif

directory = r'/Users/andrew/Downloads/'
r_exten = '.HEIC'
c=1

for filename in os.listdir(directory):
    if filename.endswith(r_exten):
        c += 1
        heif_file = pyheif.read(directory + filename)
        name = filename.replace(r_exten, ".jpg")
        image = Image.frombytes(mode=heif_file.mode, size=heif_file.size, data=heif_file.data)
        image.save(directory + name, "JPEG")
        print(os.path.join(directory, filename))
        continue
    else:
        continue
image.save

#It works, as of 10-29-20 running python 3.8 on pycharm.

