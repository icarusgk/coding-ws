import time

current_time = time.gmtime() # returns a struct_time object
action = 'to feed the cat'
print(f"It's {current_time}. Time {action}.")

# * asctime()
# we can use asctime() to convert the values to string
normal_time = time.asctime(current_time)

print(f"It's {normal_time}. Time {action}.")

# or we can indicate the value we want to give the string with directives
current_time = time.strftime("%H:%M", time.localtime()) 
print(f"It's {current_time}. Time {action}.")

# * time()
action2 = 'to feed the dog'
# Most often sleep() is used when you need some time to pass between code executions.
time.sleep(1)

current_time = time.strftime("%H:%M", time.localtime())

print(f"It's {current_time}. Time {action2}")

# * time()
# It's a float object, but you can quickly convert it into a string of the same format as
# asctime() using ctime()

print(time.asctime())          # Thu Feb 24 16:00:35 2022
print(time.ctime(time.time())) # Thu Feb 24 16:00:35 2022

# * gmtime() with argument
print(time.gmtime(0)) 
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

# ? Time difference
last_time = time.time()
current_time = time.strftime("%H:%M", time.localtime())

print(f"It's {current_time}. Time {action}")

time.sleep(1) # 1 sec

new_current_time = time.time()
time_passed = int((new_current_time - last_time) / 60)

print(f'You have fed the cat {time_passed} minutes ago')

# ? The exact time
# perf_counter() should be used only for performance measurement.
start = time.perf_counter()

print("Oh no! This cat's breaking his diet!")

end = time.perf_counter()
total_time = end - start

print(f"Your program has executed for {total_time} seconds.")


# ? Timezones
print(time.timezone / 3600) # 6.0
print(time.tzname) # ('CST', 'CST')