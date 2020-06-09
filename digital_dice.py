#dice game code
import random
import time
import sys
min = 1
max = 6
roll_again = "yes"
print("\n\tWELCOME TO DICE SIMULATOR!!")
print("\n\tWHERE YOU GET RANDOM NUMBERS FROM 1-6!!")
#arduino code using pyfirmata
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
while roll_again == "yes" or roll_again == "y" or roll_again == "Y" :
    randnum =random.randint(min,max)
    if randnum == 1:
        digi1()
    elif randnum == 2:
        digi2()
    elif randnum == 3:
        digi3()
    elif randnum == 4:
        digi4()
    elif randnum == 5:
        digi5()
    elif randnum == 6:
        digi6()
    roll_again = input("Do you wanna continue-y/n:")
board.exit()
