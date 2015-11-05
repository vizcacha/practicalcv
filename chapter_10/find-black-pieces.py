from SimpleCV import Image
import time

# Get the template and image
goBoard = Image('go.png')
black = Image('go-black.png')

black.show()
time.sleep(3)
goBoard.show()
time.sleep(3)

# Find the matches and draw them
matches = goBoard.findTemplate(black)
matches.draw()

# Show the board with matches print the number
goBoard.show()

print str(len(matches)) + " matches found."
# Should output:  9 matches found.

time.sleep(3)