import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5))
print(next(list_job))

# list_job = [longtime_job() for i in range(5)]
# print(list_job[0])