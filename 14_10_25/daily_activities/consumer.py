import time
import random

def consumer(q):
    while True:
        item=q.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(random.uniform(1,2))
    print(f"Finished")