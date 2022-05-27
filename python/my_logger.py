import sys
import io

output = io.StringIO()

class Logger:
    def __init__(self):
        self.console = sys.stdout
        self.input = sys.stdin
        self.log = output
   
    def write(self, text):
        self.console.write(text)
        self.log.write(text)


    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

sys.stdout = Logger()
sys.stdin = LogIn()

print("hi there!")
print("hi there!")
print("hi there!")
print("hi there!")
print("Enter your file name: ")

file_name = input()
output.write(file_name)

with open(file_name, "a") as file:
  file.write(output.getvalue())
  
