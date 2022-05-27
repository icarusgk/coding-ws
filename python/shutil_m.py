import shutil
import os
import time

file_name = 'news.txt'
copy_file_name = 'news_copy.txt'

# copyfile
print('Before operation:', os.listdir('.'))
shutil.copyfile(file_name, copy_file_name)
print('After operation:', os.listdir('.'))

# Before the operation: ['news.txt']
# After the operation: ['news.txt', 'news_copy.txt']

# copy
file_path = "/home/user/existence.pdf"
dst_folder = "/home/user/Articles"  # imagine that the folder contains 'innovative_ideas.pdf'

print(f"Before operation, Articles:", os.listdir(dst_folder))
shutil.copy(file_path, dst_folder)
print(f"After operation, Articles:", os.listdir(dst_folder))

# Before operation, Articles: ['innovative_ideas.pdf']
# After operation, Articles: ['existence.pdf', 'innovative_ideas.pdf']


# copy2 to preserve the metadata
def show_metadata(my_file_path):
    stat = os.stat(my_file_path)  # returns the status of the file
    print("Mode    :", oct(stat.st_mode))
    print("Created :", time.ctime(stat.st_ctime))
    print("Accessed:", time.ctime(stat.st_atime))
    print("Modified:", time.ctime(stat.st_mtime))


file_path = "/home/user/existence.pdf"
dst_folder = "/home/user/Articles"

print("Source File:")
show_metadata(file_path)
dst_path = shutil.copy2(file_path, dst_folder)
print("\nDestination File:")
show_metadata(dst_path)

# Source File:
# Mode    : 0o100777
# Created : Sun Sep 12 13:57:22 2021
# Accessed: Sun Sep 12 13:57:22 2021
# Modified: Sun Sep 12 13:57:22 2021

# Destination File:
# Mode    : 0o100777
# Created : Mon Sep 13 00:51:21 2021
# Accessed: Sun Sep 12 13:57:22 2021
# Modified: Sun Sep 12 13:57:22 2021


# Copy file directory
# copytree()
src_path = "/home/user/Articles"

src_dir = "/home/user/Articles/python_codes"
dst_dir = "/home/user/Articles/codes"

print("Before Copying:", os.listdir(src_dir))

destination = shutil.copytree(src_dir, dst_dir)  # returns the destination (dst)
print("After Copying:", os.listdir(src_path))
print("Destination path:", destination)

# Before Copying: ['python_codes']
# After Copying: ['codes', 'python_codes']
# The destination path: /home/user/Articles/codes

# Note: the destination directory should not exist


# For removing directories you can use the rmtree()
shutil.rmtree("/home/user/Articles")
# If the path does not exist, FileNotFoundError will be raised



# * Moving and finding files
# ? shutil.move()
# Takes the source and destination paths as the parameters and returns the absolute
# path of the new location

src_path = '/home/user/Desktop/payment.txt'
dest_path = '/home/user/Desktop/payments'

dest = shutil.move(src_path, dest_path)

print(dest)
# /home/user/Desktop/payments/payment.txt


# > You can move the file to a different dir and change its filename
src_path = "/home/user/Desktop/number.txt"
dst_path = "/home/user/Desktop/math/new_number.txt"

dest = shutil.move(src_path, dst_path)
print(dest)
# /home/user/Desktop/math/new_number.txt

# > Moving an entire directory from one place to another
src_dir = "/home/user/Desktop/cars"
dst_dir = "/home/user/Desktop/vehicles"

dest = shutil.move(src_dir, dst_dir)

print(dest)
# /home/user/Desktop/vehicles/cars



# ? shutil.move()
# It finds the path to the provided executable application like Python3 or Java
path_python = shutil.which("python3")
path_java = shutil.which("java")

print(path_python, "and", path_java)
# usr/bin/python3 and /usr/bin/java


# * Making an archive
# Know the available formats

formats = shutil.get_archive_formats()

for f in formats:
    print(f)

# ('bztar', "bzip2'ed tar-file")
# ('gztar', "gzip'ed tar-file")
# ('tar', 'uncompressed tar file')
# ('xztar', "xz'ed tar-file")
# ('zip', 'ZIP file')

# ? make_archive()

directory = "/home/user/Desktop/Algorithms"
arc_name = shutil.make_archive("compressed_algo", "bztar", directory)

print(arc_name)
# /home/user/Desktop/compressed_algo.tar.bz2

