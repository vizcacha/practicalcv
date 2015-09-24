from SimpleCV import Image, Color, Display
import time

car_not_in_lot = Image("parking-no-car.png")

no_car = car_not_in_lot.crop(470,200,200,200)

without_yellow_car = no_car.colorDistance(Color.YELLOW)

displayObject = Display()

only_space = no_car - without_yellow_car
only_space = only_space.toRGB()

print only_space.meanColor()

# Show the results
only_space.save(displayObject)

while displayObject.isNotDone():
    time.sleep(0.5)
