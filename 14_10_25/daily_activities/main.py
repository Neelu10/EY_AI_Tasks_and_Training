import threading
import queue
from producer import producer
from consumer import consumer

q=queue.Queue()
producer_thread=threading.Thread(target=producer,args=(q,))
consumer_thread=threading.Thread(target=consumer,args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
print(f"All tasks completed")