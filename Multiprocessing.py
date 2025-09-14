"""
Python Multiprocessing = Running tasks in parallel on different cpu cores, bypasses GIL used for threading.
Better for cpu bound tasks (heavy cpu usage)
Multithreading = Better for IO bound tasks (waiting around)
"""
# from multiprocessing import Process, cpu_count
# import time

# def counter(num):
#     count = 0
#     while count < num:
#        count += 1
# def main():
#     print(cpu_count())
#     # start_time = time.perf_counter()

#     a = Process(target = counter, args = (500000000,))
#     b = Process(target = counter, args = (500000000,))
#     c = Process(target = counter, args = (500000000,))
#     d = Process(target = counter, args = (500000000,))

#     a.start()
#     b.start()
#     c.start()
#     d.start()

#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     print("Finished in : ", time.perf_counter(), "seconds")


# if __name__ == "__main__":
#    main()

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(f"Running on {cpu_count()} CPU cores")
    
    start_time = time.perf_counter()

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))
    c = Process(target=counter, args=(500000000,))
    d = Process(target=counter, args=(500000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    end_time = time.perf_counter()
    print(f"Finished in: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()