import time
import random

def producer(q):
    for i in range(5):
        item=f"Item{i}"
        q.put(item)
        print(f"Produced:{item}")
        time.sleep(random.uniform(0.5, 1.5))
    q.put(None)
    print(f"Finished")