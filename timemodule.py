import time
# print(time.ctime(1000000))  # Convert a time expressed in seconds since epoch to a readable string
#                       # epoch = When your computer thinks time began

# print(time.time())  # returns current seconds since epoch
# print(time.ctime(time.time()))

# time_object = time.localtime()
# time__object = time.gmtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)
# print(time__object)

# time_string = "4 June, 2025"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2025,6, 7, 20, 45, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2025,6, 7, 20, 45, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)