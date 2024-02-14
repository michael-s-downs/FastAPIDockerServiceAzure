import os
import shutil

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
    
def getFolderInfo(folder_path):
    if is_folder_existant(folder_path):
        folderSize = get_folder_size(folder_path)
        return {
            "isDBPresent": True,
            "DBSize" : folderSize
            }
    else:
        return {
            "isDBPresent": False,
            "DBSize" : 0
            }
           