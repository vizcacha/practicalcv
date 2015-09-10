from SimpleCV import Kinect, Display
import time

# Initialize the Kinect
kin = Kinect()

# Initialize the display
disp = Display((640,480))

# This should be adjusted to set how many pixels
# represent an inch in the system's environment
pixelsToInches = 6

while not disp.isDone():
    img = kin.getDepth()
    blobs = img.binarize().findBlobs()
    if blobs:
        img.drawText(str(blobs[-1].height() / pixelsToInches) + " inches", 10, 10)
    img.save(disp)
    time.sleep(1)
