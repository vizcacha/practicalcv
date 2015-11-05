from SimpleCV import Camera, Display
import time

cam = Camera()

disp = Display(cam.getImage().size())

while disp.isNotDone():
	img = cam.getImage()
	
	# Look for a face
	faces = img.findHaarFeatures('face')
	
	if faces is not None:
		# Get the largest face
		faces = faces.sortArea()
		biggestFace = faces[-1]
		
		# Draw a green box around the face
		biggestFace.draw()
		
		#print bigFace
		
		noses = img.findHaarFeatures('nose')
		if noses is not None:
			noses = noses.sortArea()
			theNose = noses[-1]
		
		#	theNose.draw()
	
		eyes = img.findHaarFeatures('eye')
		if eyes is not None:
			eyes = eyes.sortArea()
			eye1 = eyes[-1]
			eye2 = eyes[0]
			
			eye1.draw()
			eye2.draw()
	
	img.save(disp)
	
