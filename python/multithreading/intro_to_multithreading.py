import time
import _thread
from threading import Thread

locks = []

def greet(lockobject):
    time.sleep(3)
    print('Hello, ')
    # Release the lock as we are done here
    lockobject.release()


# Then when we need to create a thread, where we can execute our
# function. When the thread is started, it takes the function
# and a tuple of lock objects

def create_thread():
  # Create a lock and acquire it
  lockobject = _thread.allocate_lock()
  lockobject.acquire()

  # Store it in the global lock list
  locks.append(lockobject)
  # Pass it to a new thread that can release (as a tuple)
  _thread.start_new_thread(greet, (lockobject, ))


# A lock can be either locked or unlocked. It has only two basic methods
# acquire() and release().

# When the state is unlocked, acquire() changes the state to locked and returns
# immediately. When it is locked, acquire() blocks it until a call to release()
# in another thread changes it to unlocked, then the acquire() call resets it
# to locked and returns.

# We call the release() method only when the state is locked; it changes the 
# the state to unlocked and returns immediately. If an attempt is made to
# release an unlocked lock, an error will be raised.

# Finally we can call the create_thread function and print the rest of the
# greeting message

create_thread()
print('world!')

# Acquire all locks = release all threads
all(lock.acquire() for lock in locks)



# * The threading module

def greet():
  time.sleep(3)
  print('Hello, ')


# A target is a callable object that is invoked by thread methods
t = Thread(target=greet)
t.start()

print('world!')

# our program does not wait until the delay but rather goes
# and executes the next lines.


