# Create n number of numbered files inside a dir 

import os

def create_files(directory, name, extension, n):
    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, n+1):
        filename = os.path.join(directory, f"{name}{i}.{extension}")
        with open(filename, 'w') as f:
            f.write("File number: " + str(i))


directory = input("Write the folder path: ")
fileName = input("Write the file name: ")
extension = input("Write the file extension: ")
if extension[0] == '.': extension = extension[1::]
n = int(input("Write the number of files: "))
create_files(directory, fileName, extension, n)
