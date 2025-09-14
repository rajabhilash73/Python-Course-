"""
thread = a flow of execution. Like a separate order of instructions.
However, each thread takes turn running to achieve concurrency
GIL = Global interpreter lock
allows only one thread to hold the control of the python interpreter.

# Cpu bound = program / tasks spend most of its time waiting for internal events (cpu intensive)
use multiprocessing.
Io bound = program / tasks spend most of its time waiting for external events (user input, web scrapping)
use multithreading.
"""
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You are eating breakfast.")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee.")

def study():
    time.sleep(5)
    print("You finished your study.")

x = threading.Thread(target = eat_breakfast, args = ())
x.start()

y = threading.Thread(target = drink_coffee, args = ())
y.start()

z = threading.Thread(target = study, args = ())
z.start()

x.join()
y.join()
z.join()


# eat_breakfast()
# drink_coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())