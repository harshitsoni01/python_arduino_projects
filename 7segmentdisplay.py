from pyfirmata import Arduino, util
import time 

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

a = board.get_pin("d:7:o")
b = board.get_pin("d:6:o")
c = board.get_pin("d:5:o")
d = board.get_pin("d:11:o")
e = board.get_pin("d:10:o")
f = board.get_pin("d:8:o")
g = board.get_pin("d:9:o")
dp = board.get_pin("d:4:o")

def digi1():
    b.write(1)
    c.write(1)
    a.write(0)
    g.write(0)
    e.write(0)
    d.write(0)
    f.write(0)
def digi2():
    a.write(1)
    b.write(1)
    g.write(1)
    e.write(1)
    d.write(1)
    c.write(0)
    f.write(0)
def digi3():
    a.write(1)
    b.write(1)
    g.write(1)
    c.write(1)
    d.write(1)
    e.write(0)
    f.write(0)
def digi4():
    f.write(1)
    g.write(1)
    b.write(1)
    c.write(1)
    a.write(0)
    d.write(0)
    e.write(0)
def digi5():
    a.write(1)
    f.write(1)
    g.write(1)
    c.write(1)
    d.write(1)
    b.write(0)
    e.write(0)
def digi6():
    a.write(1)
    f.write(1)
    g.write(1)
    c.write(1)
    d.write(1)
    e.write(1)
    b.write(0)

while True:
    digi1()
    time.sleep(1)
    digi2()
    time.sleep(1)
    digi3()
    time.sleep(1)
    digi4()
    time.sleep(1)
    digi5()
    time.sleep(1)
    digi6()
    time.sleep(1)
board.exit()




    
