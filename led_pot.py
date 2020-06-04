from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

led = board.get_pin("d:9:o")
pot = board.get_pin("a:1:i")

while True:
    # inputvalue = board.analog("a:1:i").read()
    # inputvalue = int(inputvalue)
    # print(inputvalue)
    # if  inputvalue is not None:
    #     led.write(inputvalue)
    # time.sleep(1)
    sensor_value = pot.read()
    print(sensor_value)
    led.write(sensor_value)
board.exit()