import os
try:
    os.mkdir("backup")
    print("folder created successfully!")
except FileExistsError:
    print("folder already exists! doing nothing")


import os
try:
    os.rmdir("temp_data")
    print("folder removed successfully!")
except FileNotFoundError:
    print("folder doesn't exists! doing nothing")

    