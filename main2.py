#设备2（sta）
import apsta_uart

sta=apsta_uart.STA()
sta.seek_host()
sta.read_thread()  #开辟另一个线程监听消息并打印
sta.send_thread()
