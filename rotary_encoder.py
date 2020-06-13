from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

clk = board.get_pin("d:2:i")
dt = board.get_pin("d:3:i")
sw = board.get_pin("d:4:o")

def encoder():
    oldA = 1
    oldB = 1
    result = 0
    newA = clk.read()
    newB = dt.read()
    if newA != oldA or newB != oldB:
        if oldA == 1 and newA == 0:
            result = oldB*2-1
    oldA = newA
    oldB = newB
    return result
encoderval = 0
change = 0
while True:
    sw.write(1)
    change = encoder()
    encoderval = encoderval + change
    if sw.read() == 0:
        encoderval = 0
    print(encoderval)
    #time.sleep(1)