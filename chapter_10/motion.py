from SimpleCV import Camera, Color, Display
import time

cam = Camera()

previous = cam.getImage()

disp = Display(previous.size())

while not disp.isDone():
	current = cam.getImage()
	motion = current.findMotion(previous)
	for m in motion:
		m.draw(color=Color.RED, normalize=False)
		
	current.save(disp)
	previous = current