from pyfirmata import Arduino, util
import time

board = Arduino("COM4")
it = util.Iterator(board)
it.start()

led = board.get_pin("d:9:o")
pot = board.get_pin("a:1:i")#use analog pins to read sensors

while True:
    sensor_value = pot.read()
    print(sensor_value)#if its showing none type then add str()
    led.write(sensor_value)
board.exit()