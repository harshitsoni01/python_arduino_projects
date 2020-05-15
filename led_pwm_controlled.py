from pyfirmata import Arduino,util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

led = board.get_pin("d:9:o")

# for a in range(0,255):
#     led.write()
#     time.sleep(0.8)

# for a in range(255,0):
while True:
    a = 0
    while a<=255:
        led.write(a)
        time.sleep(0.008)
        a+=1
    while a>=0:
        led.write(a)
        time.sleep(0.008)
        a-=1
    time.sleep(0.9)
board.exit()



