from SimpleCV import Color, Camera, Display, RunningSegmentation
import time

cam = Camera()
rs = RunningSegmentation(0.9,(99,99,99))

size = (cam.getImage().size())
disp = Display(size)

# Start the crosshairs in the center of the screen
center = (size[0] / 2, size[1] / 2)

while disp.isNotDone():
	input = cam.getImage()
	# Assume using monitor mounted camera, so flip to create mirror image
	input = input.flipHorizontal()
	rs.addImage(input)   #
	
	if(rs.isReady()):
		# Get the object that moved
		img = rs.getSegmentedImage(False)   #
		blobs = img.dilate(10).findBlobs()
		
		# If an object in motion was found
		if( blobs is not None ):
			blobs = blobs.sortArea()
			# Update the crosshairs onto the object in motion
			center = (int(blobs[-1].minRectX()),
					  int(blobs[-1].minRectY()))
					  
		# Inside circle
		input.dl().circle(center, 50, Color.BLACK, width = 3)   #
		# Outside circle
		input.dl().circle(center, 200, Color.BLACK, width = 6)
		
		# Radiating lines
		input.dl().line((center[0], center[1] - 50),
			(center[0], 0), Color.BLACK, width = 2)
		input.dl().line((center[0], center[1] + 50),
			(center[0], size[1]), Color.BLACK, width = 2)
		input.dl().line((center[0] - 50, center[1]),
			(0, center[1]), Color.BLACK, width = 2)
		input.dl().line((center[0] + 50, center[1]),
			(size[0], center[1]), Color.BLACK, width = 2)
		
		input.save(disp)