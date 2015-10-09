__author__ = 'becks'
import time
from SimpleCV import Image

head = Image('head.png')

amgothic = Image('amgothic.png')

scream = Image('scream.png')

amgothic.dl().blit(head,(175, 110))

amgothic.show()

time.sleep(2)

layer = amgothic.getDrawingLayer()

scream.addDrawingLayer(layer)

scream.show()
time.sleep(2)

print amgothic._mLayers
print scream._mLayers

layer.blit(head,(75,220))

amgothic.show()
time.sleep(2)
scream.show()

time.sleep(5)
