__author__ = 'becks'

import time
from SimpleCV import Camera, Image, Color, Display

img = Image((300, 300))

img.dl().circle((150, 75), 50, Color.RED, filled = True)

img.dl().line((150, 125), (150, 275), Color.WHITE, width = 5)

img.show()

time.sleep(5)

cam = Camera()

size = cam.getImage().size()

disp = Display(size)

center = (size[0] / 2, size[1] / 2)

while disp.isNotDone():
    img = cam.getImage()

    img.dl().circle(center, 50, Color.BLACK, width = 3)

    img.dl().circle(center, 200, Color.BLACK, width = 6)

    img.dl().line((center[0], center[1] - 50), (center[0], 0), Color.BLACK, width = 2)
    img.dl().line((center[0], center[1] + 50), (center[0], size[1]), Color.BLACK, width = 2)
    img.dl().line((center[0] - 50, center[1]), (0 , center[1]), Color.BLACK, width = 2)
    img.dl().line((center[0] + 50, center[1]), (size[0], center[1]), Color.BLACK, width = 2)

    img.save(disp)
