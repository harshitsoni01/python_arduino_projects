from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

sw = board.get_pin("d:3:i")
led = board.get_pin("d:13:o") 

while True:
    value = sw.read()
    if value == 1:
         led.write(1)
    else:
        led.write(0)
board.exit()

