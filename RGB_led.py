from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

red = board.get_pin("d:11:o")
green = board.get_pin("d:10:o")
blue = board.get_pin("d:9:o")

def led_red():
    red.write(1)
    green.write(0)
    blue.write(0)
def led_green():
    red.write(0)
    green.write(1)
    blue.write(0)
def led_blue():
    red.write(0)
    green.write(0)
    blue.write(1)
def white():
    red.write(1)
    green.write(1)
    blue.write(1)
#create as many colors you want by mixing leds
while True:
    led_red()
    time.sleep(1)
    led_green()
    time.sleep(1)
    led_blue()
    time.sleep(1)
    white()
    time.sleep(1)

board.exit()