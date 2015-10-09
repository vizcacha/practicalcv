__author__ = 'becks'
from SimpleCV import Display, Camera, Image

display = Display(resolution=(800,400))

cam = Camera(0,{'width': 320, 'height': 240})

img = cam.getImage()

img.save(display)

# Should print: (320, 240)
print img.size()
