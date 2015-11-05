from SimpleCV import Color, Camera, Display, Image
import time

cam = Camera()
disp = Display(cam.getImage().size())

# Load the stache and alpha mask
stache = Image("mustache.png")
mask = stache.createAlphaMask()

while disp.isNotDone():
	img = cam.getImage()
	
	faces = img.findHaarFeatures('face')
	if( faces is not None ):
		# Get the biggest face
		face = faces.sortArea()[-1]
		myface = face.crop()
		
#		myface.show()
		
		noses = myface.findHaarFeatures('nose')
		# If we have a nose
		if( noses is not None):
			nose = noses.sortArea()[-1]
			
			# Calculate the mustache position
			xmust = face.points[0][0] + nose.x + (stache.width/2)
			ymust = face.points[0][1] + nose.y + (2*nose.height()/3)
			
			# Blit the stache/mask onto the image
			img = img.blit(stache,pos=(xmust,ymust), mask=mask)
			
		img.save(disp)

time.sleep(3)