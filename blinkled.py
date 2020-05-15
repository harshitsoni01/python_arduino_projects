from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()
print("Hello!Arduino")
LED = board.get_pin("d:13:o")

while True:
    LED.write(1)
    time.sleep(0.5)
    LED.write(0)
    time.sleep(0.5)

board.exit()
