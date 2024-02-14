import datetime
import os
import shutil
from models import HelpDBState

def delete_folder_if_exists(folder_path):
    if is_folder_existant(folder_path):
        shutil.rmtree(folder_path)

def is_folder_existant(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False
    
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size  

def get_last_update_timestamp(folder_path: str) -> str:

    # Initialize the latest modification time to epoch 0
    latest_mod_time = 0

    # Walk through all files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            mod_time = os.path.getmtime(file_path)
            # Update latest_mod_time if the current file's mod_time is newer
            if mod_time > latest_mod_time:
                latest_mod_time = mod_time

    # Convert the latest modification time to a datetime object
    last_update_datetime = datetime.fromtimestamp(latest_mod_time)

    # Format the datetime object as a string in the format "YYYY-MM-DD HH:MM:SS"
    last_update_str = last_update_datetime.strftime("%Y-%m-%d %H:%M:%S")

    return last_update_str  
    
def getHelpDBState(folder_path) -> HelpDBState:
    if is_folder_existant(folder_path):
        folder_size = get_folder_size(folder_path)
        last_update_str = get_last_update_timestamp(folder_path)
        return HelpDBState(True, folder_size, last_update_str)
    else:
        return HelpDBState(False,0) 
           