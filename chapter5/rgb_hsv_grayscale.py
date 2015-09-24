from SimpleCV import Image, Display
import time

displayObject = Display()

img = Image('starry_night.png')

print 'Initial: %s' % (img.getPixel(25, 25),)

img.save(displayObject)

time.sleep(3)

hsv = img.toHSV()

print 'HSV: %s' % (hsv.getPixel(25, 25),)

hsv.save(displayObject)

time.sleep(3)

rgb = hsv.toRGB()

print 'RGB: %s' % (rgb.getPixel(25, 25),)

rgb.save(displayObject)

time.sleep(3)

gray = img.grayscale()

print 'Grayscale: %s' % (gray.getPixel(25, 25),)

gray.save(displayObject)

time.sleep(3)
