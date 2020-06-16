from pyfirmata import Arduino,util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

xpin = board.get_pin("a:0:i")
ypin = board.get_pin("a:1:i")
zpin = board.get_pin("a:2:i")

while True:
    x = xpin.read()
    time.sleep(0.001)
    y = ypin.read()
    time.sleep(0.001)
    z = zpin.read()
    time.sleep(0.001)

    print(str(x)+"\t" +str(y)+ "\t" +str(z))
    time.sleep(1)
board.exit()