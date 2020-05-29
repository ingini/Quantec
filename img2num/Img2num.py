from PIL import Image
import sys
import numpy as np

fImg = sys.argv[1]

img = Image.open(fImg)
im = img.load()
#print(img.size)
(width, height) = img.size

i2n = np.ones((width, height)).tolist()

for i in range(0, width):
    for j in range(0, height):
        (r, g, b) = im[i,j]
        i2n[i][j] = [r, g, b]

fName = sys.argv[1]

fName = fName[0:-4] + '_output.txt'

sys.stdout = open(fName,'w')
print(i2n)
