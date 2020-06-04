from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

red = board.get_pin("d:11:o")
green = board.get_pin("d:10:o")
blue = board.get_pin("d:9:o")

while True:
    red.write(1)
    time.sleep(1)
    green.write(1)
    time.sleep(1)
    blue.write(1)
    time.sleep(1)
    red.write(0)
    time.sleep(1)
    blue.write(0)
    time.sleep(1)
    green.write(0)
    time.sleep(1)

board.exit()