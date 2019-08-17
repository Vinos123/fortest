import time
import machine # Need to be Init
from machine import UART

uart = UART(2, baudrate=9600,rx=16, tx=17)

#while 1:

if 1:
  aa='1'
  uart.write(aa.encode())
  print("send:"+aa)

  if uart.any():
    recv=uart.read().decode()
    print('received: ' + recv + '\n')
  
  time.sleep(3)
  
