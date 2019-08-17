from myb.serial_uart import uart
import time 

com = uart(27, 34, False, 512)  #tx=27, rx=34
com.open(9600)

while True:
    time.sleep(1)
    if com.any() > 0:
        print(com.read().decode())
    
    com.write(b'123')




# >>> from myb.serial_uart import uart
# >>> import time
# >>>
# >>> com = uart(27, 34, False, 512)  #tx=27, rx=34
# >>> com.open(9600)
# 0
# >>> com.write(b'abc')
# 3
# >>> com.read()
# b'qwe'