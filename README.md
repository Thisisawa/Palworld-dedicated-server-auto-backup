# 帕魯專用伺服器自動備份程式
適用於windows系統的自動備份程式，依照設定時間自動備份遊戲世界檔案，不包含重啟功能  

放置於伺服器根目錄執行即可  
```
py start.py
```
這個程式會在伺服器關閉時自動關閉，所以可以放在背景執行
```
pythonw start.py
```
### 設定值
根據你的需求更改程式內容  

目標資料夾  
```
target_folder = "Pal\Saved\SaveGames/0"
```  
備份檔資料夾  
```
backup_files_folder = "Pal\Saved\SaveGames"
```  
備份檔數量  
```
file_count = 5
```  
備份間隔(秒)  
```
interval = 60
```  

# Palworld dedicated server backupper
This script is for hosting server on Windows. It will backup the save folder to a RAR file. 

Put in server directory and run
```
py start.py
```  
The script will terminate when server shuts down, so you can run this script in the background.  
```
pythonw start.py
```
### Settings
Modify these value according to your needs

Target folder
```
target_folder = "Pal\Saved\SaveGames/0"
```  
Backup file folder
```
backup_files_folder = "Pal\Saved\SaveGames"
```  
Number of backup file keeps
```
file_count = 5
```  
Backup interval (seconds)
```
interval = 60
```  
