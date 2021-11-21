#need to be resolved
#it hasn't been connected to a arduino board
from pyfirmata import Arduino,util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

led = board.get_pin("a:0:i")

#buzz = board.get_pin("d:5:o")

while True:
    light = led.read()
    print(light)
    if light > 0:
        buzz = board.get_pin("d:5:o")
        buzz.write(1)
        buzz = board.get_pin("d:5:i")

board.exit()