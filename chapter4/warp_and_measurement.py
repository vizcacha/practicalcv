from SimpleCV import Image

img = Image('skew.png')

# Warp the picture to straighten the paper
corners = [(0,0), (480,0), (336,237), (147,237)]

warped = img.warp(corners)

# Find the blob that represents the paper
bgcolor = warped.getPixel(240,115)

dist = warped.colorDistance(bgcolor)

blobs = dist.invert().findBlobs()

paper = blobs[-1].crop()

# Find the blob that represents the toy
toyBlobs = paper.invert().findBlobs()

toy = toyBlobs[-1].crop()
