from pyfirmata import Arduino,util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

s1 = board.get_pin("d:2:o")
s2 = board.get_pin("d:6:o")
s3 = int(s1)
s4 = int(s2)
while True:
    for x in range(s3,s4):
        s1.write(1)
    for x in range(s4,s3):
        s1.write(0)
    for x in range(s3,s4):
        s1.write(1)
    for x in range(s4,s3):
        s1.write(0)
    s3 +=1

   