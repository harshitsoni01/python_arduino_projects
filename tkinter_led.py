from pyfirmata import Arduino, util
from tkinter import *

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

led = board.get_pin("d:13:o")
m = Tk() 


def led_on():
    while True:
        led.write(1)
        refresh(m)#this causes a problem which can removed by removing 'm' 
#but then the window will close after one click  

def led_off():
    while True:
        led.write(0)
        refresh(m)

m.title("GUI + Arduino")
m.geometry("100x100")#pady for grid and themes for tkinter. To get themes pip install ttkthemes
thelabel = Label(m, text = "Welcome to led simulation!")
thelabel.pack(side = TOP)

btn1 = Button(m, text = "ON", command = led_on )
btn1.pack(side = LEFT)
btn2 = Button(m, text = "OFF", command = led_off)
btn2.pack(side = LEFT)
def refresh(window):
    window.destroy()
    window.__init__()
m.mainloop()
board.exit()