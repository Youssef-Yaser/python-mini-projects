# =========================
#  Automated File Backup 
# =========================

import os
import shutil
import datetime
import schedule
import time

# =========================
# Terminal Colors
# =========================
class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

# =========================
# Game Header
# =========================
print(f"{Color.GREEN}{Color.BOLD}")
print("==================================")
print("        Automated File Backup     ")
print("==================================")
print(f"{Color.END}")


source_dir="/home/youssef-yaser/Documents/Vscode_Projects/Projects_To_Learn_Python/02-Intermediate/ Automated File Backup"

destination_dir ="/home/youssef-yaser/Pictures"

def copy_folder_to_directory(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try :
        shutil.copytree(source,dest_dir) 
        print(f"Floder copied to : {dest_dir}")
    except FileExistsError :
        print(f"Folder already exists in : {dest_dir}")   



schedule.every().day.at("16:08").do(lambda : copy_folder_to_directory(source_dir, destination_dir))

while True  :
    schedule.run_pending()
    time.sleep(60)