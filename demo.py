from pathlib import Path

from PIL import Image

im = Image.open(r'data\processed\Rice Leaf Disease Images\Bacterialblight\BACTERAILBLIGHT3_002.jpg')
print(im.size)
im1 = im.resize((64, 64))
im1.show()