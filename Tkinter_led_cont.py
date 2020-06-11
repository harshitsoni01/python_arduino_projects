from pyfirmata import Arduino, util
from tkinter import *
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

red = board.get_pin("d:13:o")
white = board.get_pin("d:12:o")
yellow = board.get_pin("d:11:o")
m = Tk()#to create tkinter window
#function for different led
def led(args):
    if args == 1:
        while True:
            red.write(1)
            refresh()
    if args == 2:
        while True:
            red.write(0)
            refresh()           
    if args == 3:
        while True:
            white.write(1)
            refresh()
    if args == 4:
        while True:
            white.write(0)
            refresh()
    if args == 5:
        while True:
            yellow.write(1)
            refresh()
    if args == 6:
        while True:
            yellow.write(0)
            refresh()
#tkinter code 
m.title("GUI + Arduino")
m.geometry("600x600")#size of the window # its "x" not "*"
thelabel = Label(m, text = "Welcome to led simulation!")
thelabel.pack(side = TOP)
b1 = Button(m, text = "RED LED ON", command = lambda: led(1)) # if the fucntions were definded individually/n
b1.pack(side=LEFT)  #b1 = Button(m, text = "RED LED", command = red_led )
b2 = Button(m, text = "RED LED OFF", command = lambda: led(2))
b2.pack(side=LEFT)
b3 = Button(m, text = "WHITE LED ON", command = lambda: led(3))
b3.pack(side=RIGHT)
b4 = Button(m, text = "WHITE LED OFF", command = lambda: led(4))
b4.pack(side=RIGHT)
b5 = Button(m, text= "YELLOW LED ON", command = lambda: led(5))
b5.pack()
b6 = Button(m, text = "YELLOW LED OFF", command = lambda: led(6))
b6.pack()

def refresh(m):#function to refresh the window after every button click so the window doesn't close
    m.destroy()
    m.__init__()
m.mainloop()
 
board.exit()