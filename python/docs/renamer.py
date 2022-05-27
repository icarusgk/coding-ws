#!/bin/python
import os
import sys

file_names = [
  "This is a normal file",
  "This is another normal file",
  "Normal file with spaces here",
  "Another complete normal file",
  "Final normal file to process"
]

def add_lowerdash(file_names: list):
  for f in file_names:
    os.rename(f, f.replace(" ", "_"))

def go_back(files_names: list):
  for f in files_names:
    os.rename(f, f.replace("_", " "))

def main():

  args = sys.argv
  
  if len(args) != 2:
    print("error!")
    sys.exit()

  directory = args[1]
  
  
  file_names = os.listdir()
  
  while True:
    print("""
    1. Add lowerdashes
    2. Go back to normal
    """)
    choice = int(input("Enter an option: "))
    
    if choice == 1:
      add_lowerdash(file_names)
    
    if choice == 2:
      go_back(file_names)

    if choice == 3:
      break


if __name__ == "__main__":
  main()
