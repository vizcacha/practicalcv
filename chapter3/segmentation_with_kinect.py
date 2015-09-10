from SimpleCV import Kinect
import time

# Initialize the Kinect
kin = Kinect()

# Get the image and depth information
dep = kin.getDepth()
img = kin.getImage()

# Turn into a pure black and white image for segmentation
fore = dep.binarize(190).invert()
fore_only = img - fore

fore_only.show()

# Keep the image open for 10 seconds
time.sleep(10)
