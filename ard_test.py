#this is used to check the running voltage of arduino.
#use try and except to install pyfirmata 
#if you already don't have it
try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util

import time
board = Arduino("COM4")#select port acccording to your PC and OS

it = util.Iterator(board)#it will be used to read the status of the inputs of the circuit.
it.start()#starts the iterator

Tv1 = board.get_pin('a:0:i')#("'a'nalog/'d'igital:pin number:'i'nput/'o'utput/'p'wm")
#this sets pin 0 as a analog input 
time.sleep(1)
print(Tv1.read())#read() to read the data from arduino
