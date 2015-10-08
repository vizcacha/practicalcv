from SimpleCV import Camera, Color, Display, Image

cam = Camera()
original_background = Image('weather.png')

disp = Display()

while not disp.isDone():
    img = cam.getImage()
    img = img.flipHorizontal()
    
    bgcolor = img.getPixel(10, 10)
    dist = img.colorDistance(bgcolor)
    mask = dist.binarize(50)
    
    foreground = img - mask

    background = original_background - mask.invert()

    combined = background + foreground

    combined.save(disp)
