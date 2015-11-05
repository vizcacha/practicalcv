from SimpleCV import Image, Color
img = Image("puzzle.jpg")
blobs = img.binarize().findBlobs()
blobs.image = img
blobs[-1].drawHull(color=Color.RED)
img.show()