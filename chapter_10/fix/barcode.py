from SimpleCV import Color, Camera, Display
import time

cam = Camera()
display = Display()

message = "Last item scanned: "
result = "None"

while( display.isNotDone() ):
	img = cam.getImage()
	
	barcode = img.findBarcode()
	if( barcode is not None ):
		result = str(barcode.data)
		
	img.drawText(message + result, color=Color.GREEN, fontsize=40)
	
	img.save(display)

time.sleep(3)