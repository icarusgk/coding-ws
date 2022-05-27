 
import os

# Current working directory
div_result = int(input()) / int(input())

# file = open('division_result.txt', 'w', encoding='utf-8')
# file.write(str(div_result))
# file.close()

print("The current working directory is: ", os.getcwd())
os.chdir('/home/user')
os.mkdir('new_project')
os.mkdirs('new/project')
os.listdir('new_project')
os.rename('new_project', 'final_project')

# Access
# The mode os.F_OK is used to check the specified path for existence
os.access('new_project', os.F_OK) # True

# Permissions with
# R_OK W_OK X_OK

os.access('/home/user', os.R_OK)

os.remove('new_project/main.py') # removing files
os.rmdir('new_project') # has to be empty


os.path.split('/home/icarusgk/coding-ws')
# ('/home/icarusgk', 'coding-ws')

os.path.dirname('/home/icarusgk/coding-ws')
# '/home/icarusgk'

os.path.basename('/home/icarusgk/coding-ws')
# 'coding-ws'

os.path.isdir('/home/icarusgk/coding-ws')
# True

os.path.isfile('/home/icarusgk/coding-ws')
# False