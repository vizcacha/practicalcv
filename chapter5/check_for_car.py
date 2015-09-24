from SimpleCV import Image, Color, Display
import argparse

parser = argparse.ArgumentParser(description='Check for car in handicap spot.')
parser.add_argument('img')
args = parser.parse_args()
img = args.img

image = Image(img)

cropped_image = image.crop(470,200,200,200)

color_distance = cropped_image.colorDistance(Color.YELLOW)

spot = cropped_image - color_distance
spot = spot.toRGB()

(r, g, b) =spot.meanColor()

if ((r>15) and (g>10)):
    print "The car is in the lot. Call the attendant."
else:
    print "The car is not in the lot."
