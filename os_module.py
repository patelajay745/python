import os

home_directory = os.path.expanduser("~")
# print(f"\nContents of Home Directory ({home_directory}):")
print(os.listdir(home_directory+"/Desktop/"))

