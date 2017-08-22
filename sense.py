from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

tmax = 32
tmin = 8

while True:
    temp = sense.get_temperature()
    print(temp)
    temp = int(temp/4) - tmin
    for x in range(0, 8):
        for y in range(0, temp):
            sense.set_pixel(x, y, 255, 0, 0)
        for y in range(temp, 8):
            sense.set_pixel(x, y, 0, 0, 0)