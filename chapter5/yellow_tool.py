from SimpleCV import Image, Color
import time

yellowTool = Image('yellowtool.png')

yellowDist = yellowTool.colorDistance((223, 191, 29))

yellowDist.show()
time.sleep(3)

yellowDistBin = yellowDist.binarize(50).invert()

yellowDistBin.show()
time.sleep(3)

onlyYellow = yellowTool - yellowDistBin

onlyYellow.show()
time.sleep(3)
