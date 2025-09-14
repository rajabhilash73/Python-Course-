"""
Demon Thread = A thread that runs in the background not important for program to run
your program will not wait for demon threads to complete before exiting
non-demon threads cannot normally be killed stay alive until the task is complete.

Ex - background tasks, garbage collection, waiting for input, long-running process.
"""

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for : ", count, "seconds")
x = threading.Thread(target = timer, daemon = True)
x.start()

x.setDaemon(True)
print(x.isDaemon())


answer = input("Do you want to exit ?")