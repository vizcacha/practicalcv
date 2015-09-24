from SimpleCV import Image, Color, Display
import time

car_in_lot = Image("parking-car.png")

car = car_in_lot.crop(470,200,200,200)

yellow_car = car.colorDistance(Color.YELLOW)

only_car = car - yellow_car
only_car = only_car.toRGB()

displayObject = Display()

print only_car.meanColor()

# Show the results
only_car.save(displayObject)

while displayObject.isNotDone():
    time.sleep(0.5)
