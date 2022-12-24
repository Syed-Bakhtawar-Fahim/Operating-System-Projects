import os
import random

# p --> path of file
p = r"C:\Users\adv\Desktop\friends"
os.chdir(p)

print(os.listdir(p))

# print the current directory
# cwd = os.getcwd() 
# print("Current working directory is:", cwd)


folder_name = random.choice(os.listdir(p))

# now this come to friend/1 or friend/randomFolder
folder_path = str(os.path.realpath(folder_name))

# now this come to friend/1/file.extention or friend/randomFolder/randomFile for play
os.chdir(folder_path)

file_name = random.choice(os.listdir(folder_path))

print("Enjoy!!")

# play the file

# os.system("open" + file_name) # macbook

os.system("start " + file_name)