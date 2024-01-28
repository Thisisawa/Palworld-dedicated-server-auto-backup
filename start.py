import os
import time
import psutil
from win10toast import ToastNotifier
import subprocess
import math
import zipfile
toaster = ToastNotifier()

# 目標資料夾
target_folder = "Pal/Saved/SaveGames/0/"
# 備份檔資料夾
backup_files_folder = "Pal/Saved/SaveGames/"
# 備份檔數量
file_count = 5
# 備份間隔(秒)
interval = 300

def backup_rar(zip_path, dst_dir, backup_files):
    # 生成名稱
    zip_name = zipfile.ZipFile(dst_dir + time.strftime("%Y%m%d%H%M%S") + '.zip', 'w', zipfile.ZIP_DEFLATED)
    # 生成檔案    
    for root, dirs, files in os.walk(zip_path):
        for file in files:
            zip_name.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(zip_path, '..')))
    zip_name.close
    # list根目錄物件
    all_files = sorted(os.listdir(dst_dir))

    # 過濾
    all_backups = [file for file in all_files if file.endswith('.zip')]

    # 大於設定數量 刪除最舊檔案
    while len(all_backups) > backup_files:
        oldest_backup = all_backups.pop(0)
        os.remove(os.path.join(dst_dir, oldest_backup))

def server_health(name='PalServer.exe'):
    # 伺服器狀態
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return True
    return False

def shutdown():
    toaster.show_toast("偵測到伺服器關閉，程式已停止\n server no longer there, stop backup process")
    exit()

while True:
    time.sleep(1)
    if server_health():
        backup_rar(target_folder, backup_files_folder, file_count)
    else:
        shutdown

    for i in range(math.ceil(interval/10)):
        time.sleep(10)
        if server_health():
            print('Running')
        else:
            shutdown()
