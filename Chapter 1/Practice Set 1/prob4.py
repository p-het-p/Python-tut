import os

# Enter the path of directory you want to see what in it...
directory_path = input("Enter the path of the directory: ")

# Check the entered path is valid or not
if os.path.exists(directory_path):
    # List all files and directories in the given path
    contents = os.listdir(directory_path)
    
    print(f"\nContents of '{directory_path}':")
    for item in contents:
        print(item)
else:
    print("The specified directory does not exist.")
