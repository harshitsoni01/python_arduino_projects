from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

print("Hello!Arduino")#not necessary

LED = board.get_pin("d:13:o")#stting led to pin 13

while True:
    LED.write(1)#to give input value to LED pin
    time.sleep(0.5)
    LED.write(0)
    time.sleep(0.5)

board.exit()#to exit arduino board
