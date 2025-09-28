import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)
        
print("Start")

treads = []
for i in range(5):
    # long_task()
    t = threading.Thread(target=long_task)
    treads.append(t)

for t in treads:
    t.start()

for t in treads:
    t.join()
    
print("End")