from sense_hat import SenseHat
import time

from sheets import writeTemp

sense = SenseHat()
sense.clear()

tmax = 32

time_seconds = 10

while True:
	time.sleep(time_seconds)

    temp = sense.get_temperature()
    writeTemp(temp)    
    print(temp)

    temp = round(int(temp/4),2)

    for x in range(0, 8):
        for y in range(0, temp):
            sense.set_pixel(x, y, 255, 0, 0)
        for y in range(temp, 8):
            sense.set_pixel(x, y, 0, 0, 0)