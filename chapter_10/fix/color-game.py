from SimpleCV import ColorSegmentation, Image, Display, ImageSet
import time

redBlock = Image('redblock.png')
greenBlock = Image('greenblock.png')
blueBlock = Image('blueblock.png')

cs = ColorSegmentation()
cs.addToModel(redBlock)
cs.addToModel(greenBlock)
cs.addToModel(blueBlock)

cards = ImageSet('cards')
card = None

disp = Display((320, 240))

score = 0
isPrimary = False

while (cards or card) and disp.isNotDone():

	if card is None:
		card = cards.pop()
		
		cs.addImage(card)
		res = cs.getSegmentedImage()
		
		color = res.meanColor()
		if ((color[0] < 254) and (color[1] < 254) and (color[2] < 254)):
			isPrimary = True
		else:
			isPrimary = False
			
		card.drawText('Click left if primary, otherwise right', 0, 0)
		card.drawText(str(score) + ' correct answers', 0, 210)
		
	card.save(disp)
	
	if disp.mouseLeft:
		if isPrimary:
			card.drawText('Correct!', fontsize=30)
			score += 1
		else:
			card.drawText('Wrong!', fontsize = 30)
			
		card.save(disp)
		time.sleep(2)
		card = None
		
	if disp.mouseRight:
		if not isPrimary:
			card.drawText('Correct!', fontsize=30)
			score += 1
		else:
			card.drawText('Wrong!', fontsize = 30)
			
		card.save(disp)
		time.sleep(2)
		card = None