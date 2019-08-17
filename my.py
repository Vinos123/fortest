#设备1（ap）
import apsta

ap=apsta.AP()
ap.listen_client()
ap.read_thread() #开辟另一个线程监听消息并打印

ap.send("123")  #发送