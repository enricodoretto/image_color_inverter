from PIL import Image
import matplotlib.pyplot as plt
import glob

for filename in glob.glob('images/*'):
    img=Image.open(filename)
    
    w,h=img.size
    for i in range(w):
        for j in range(h):
            r,g,b=img.getpixel((i,j))
            r=255-r
            g=255-g
            b=255-b
            img.putpixel((i,j),(r,g,b))
            
    im1 = img.save(filename)