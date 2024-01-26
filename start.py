import os
import time
import psutil
from win10toast import ToastNotifier
import subprocess
toaster = ToastNotifier()

def backup_rar(src_dir, dst_dir, backup_files):
    # 生成名稱
    rar_name = time.strftime("%Y%m%d%H%M%S") + '.rar'
    rar_path = os.path.join(dst_dir, rar_name)

    # 生成檔案    
    command = f'"C:\Program Files\WinRAR\Rar.exe" a -r {rar_path} {src_dir}'
    subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    # list根目錄物件
    all_files = sorted(os.listdir(dst_dir))

    # 過濾rar
    all_backups = [file for file in all_files if file.endswith('.rar')]

    # 大於設定數量 刪除最舊檔案
    while len(all_backups) > backup_files:
        oldest_backup = all_backups.pop(0)
        os.remove(os.path.join(dst_dir, oldest_backup))

def server_health(name):
    # 伺服器狀態
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return True
    return False

# 目標資料夾
target_folder = "Pal\Saved\SaveGames/0"
# 備份檔資料夾
backup_files_folder = "Pal\Saved\SaveGames"
# 備份檔數量
file_count = 5
# 備份間隔(秒)
interval = 60

while True:

    time.sleep(interval)

    if server_health('PalServer.exe'):
        print('正在運行 Running')
    else:
        toaster.show_toast("偵測到伺服器關閉，程式已停止""\n" 
                           "server stopped, shutdown backup process")
        exit()

    backup_rar(target_folder, backup_files_folder, file_count)
