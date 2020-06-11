from pyfirmata import Arduino,util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

s1 = board.get_pin("d:2:o")
s2 = board.get_pin("d:3:o")
s3 = board.get_pin("d:4:o")
s4 = board.get_pin("d:5:o")
#fucntions to turn one led on and others off
def led1():
    s1.write(1)
    s2.write(0)
    s3.write(0)
    s4.write(0)
def led2():
    s1.write(0)
    s2.write(1)
    s3.write(0)
    s4.write(0)
def led3():
    s1.write(0)
    s2.write(0)
    s3.write(1)
    s4.write(0)
def led4():
    s1.write(0)
    s2.write(0)
    s3.write(0)
    s4.write(1)
while True:
    led1()
    time.sleep(1)
    led2()
    time.sleep(1)
    led3()
    time.sleep(1)
    led4()
    time.sleep(1)
board.exit()
   