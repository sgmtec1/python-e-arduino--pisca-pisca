from pyfirmata import Arduino, util
import time

board=Arduino ('COM6')

print ("Inicio")
for i in range (10):
    board.digital[7].write(1)
    time.sleep(1)
    board.digital[7].write(0)
    time.sleep(1)
print ("FIM")