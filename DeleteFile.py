import os
import shutil
path = "empty_folder"


try:
    # os.remove(path) # Deletes a file
    os.rmdir(path)  # Deletes a empty directory
    #shutil.rmtree(path) # deletes a directory containiing files
except FileNotFoundError:
    print("That file is not found.")
except PermissionError:
    print("You don't have permission to delete this file.")
except OSError:
    print("You can not delete this file because it's not empty.")
else:
    print(path + " Was deleted.")