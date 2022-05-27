import time
from threading import Thread

# * Multithreading in Python
def cube_area(thread, length, delay=0):
  time.sleep(delay)
  print(f"{thread} ---> Area of a cube with an edge length of {length} is: \t{6 * (length * 2)}")

def circle_area(thread, length, delay=0):
  time.sleep(delay)
  print(f"{thread} ---> Area of a circle with a radius length of {length} is: \t{3.14 * (length * 2)}")

# instantiate multiple threads with functions as targets and thread name, length as arguments


t1 = Thread(target=cube_area, args=("t1", 2, 3))
t2 = Thread(target=circle_area, args=("t2", 2, 2))

t3 = Thread(target=cube_area, args=("t3", 4, 1))
t4 = Thread(target=circle_area, args=("t4", 6, 2))

t5 = Thread(target=cube_area, args=("t5", 9, 4))
t6 = Thread(target=circle_area, args=("t6", 8, 3))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

# The lines with the shortest delay are printed first, while those with a 
# longer delay are printed at the end of our program

