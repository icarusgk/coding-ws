# file keyword arguments
# is in charge of where the function will write given objects to
# by default is sys.stdout the std output stream

# instead of the default value, you can specify the file parameter

def file_argument():
  my_file = open('file_argument.txt', 'w')
  print('This string will be in the file...', file=my_file)
  my_file.close()

# Alternatively, you can set file to sys.stderr
import sys

def division():
    a = int(input("Set the first number: "))
    b = int(input("Set the second number: "))
    if b != 0:
        print(a / b)
    else:
        # The string below will look like an error message.
        print("The second number cannot be a zero!", file=sys.stderr)


# * the flush argument
import time

out = open('file1.txt', 'w')

for i in range(3):
    print(i, file=out)
    time.sleep(5)

# at this moment the file is still empty because the buffer has not been flushed
out.close()
# now the numbers have appeared in the file



out2 = open('file2.txt', 'w')

for i in range(3):
    print(i, file=out2, flush=True)
    # the numbers are immediately written to the file
    time.sleep(5)

out2.close()