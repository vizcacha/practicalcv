from SimpleCV import Camera, Display

frameWeight = .2

cam = Camera()

lastImage = cam.getImage()

display = Display((int(cam.getProperty('width')), int(cam.getProperty('height'))))

while not display.isDone():
    img = cam.getImage()
    img = (img * frameWeight) + (lastImage * (1 - frameWeight))
    img.save(display)
    lastImage = img
