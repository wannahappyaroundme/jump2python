import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)
        
print("Start")

for i in range(5):
    long_task()

print("End")