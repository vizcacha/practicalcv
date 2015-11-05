from SimpleCV import Image
img = Image("tape.jpg")
blobs = img.binarize().morphClose().findBlobs()
blobs.image = img
blobs[-1].drawHoles()
img.show()