#this is used to check the running voltage of arduino.
try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util

import time
board = Arduino("COM4")
it = util.Iterator(board)
it.start()
Tv1 = board.get_pin('a:0:i')#'a'nalog/'d'igital:pin number:'i'nput/'o'utput/'p'wm
time.sleep(1)
print(Tv1.read())
