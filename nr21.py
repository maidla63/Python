# Loo kood, mis:
# leiab kataloogist kõik JPG pildid
# pöörab pildid otseks
# muudab halltoonideks (“L”)
# kärbib 350×350 pisipildiks
# salvestab kataloogi /thumb ja nummerdab nimed 1.jpg, 2.jpg jne

from PIL import Image

img = Image.open("yl_pildid")
 