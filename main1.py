#设备1（ap）
import apsta_uart

ap=apsta_uart.AP()
ap.listen_client()
ap.read_thread() #开辟另一个线程监听消息并打印
ap.send_thread() 

