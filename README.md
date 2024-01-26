# 帕魯專用伺服器自動備份程式
適用於windows系統的自動備份程式，依照設定時間自動備份遊戲世界檔案，不含重啟功能  

放置於伺服器根目錄執行即可  
## python版本說明
安裝相依
```
pip install -r requirements.txt
```
啟動
```
py start.py
```
這個程式會在伺服器關閉時自動關閉，所以可以放在背景執行
```
pythonw start.py
```
## Batch file版本說明
點擊兩下即啟動 預設背景執行 不會有視窗
移除2~4行後會顯示視窗

## 設定值
根據你的需求更改程式內容  


py備份檔資料夾  
```
backup_files_folder = "Pal/Saved/SaveGames"
```
bat備份檔資料夾
```
set main_folder="Pal/Saved/SaveGames"
```
備份檔數量  
```
file_count = 5
```  
備份間隔(秒)  
```
interval = 300
```


# Palworld dedicated server backupper
This script is for hosting server on Windows. It will backup the save folder to a RAR file. 
Will not restart server.

## Python Version
install packages
```
pip install -r requirements.txt
```
start script
```
py start.py
```  
The script will automatic terminate when server shutdown, so you can run this script in background.  
```
pythonw start.py
```
## Batch file Version
just give it two left click, this script run in background in default, will automatic terminate too.  
you can remove the 2~4 rows to cancel background mode.
### Settings
Modify these value according to your needs

py backup file folder
```
backup_files_folder = "Pal/Saved/SaveGames"
```
bat backup file folder
```
backup_files_folder = "Pal/Saved/SaveGames"
```  
Number of backup file keeps
```
file_count = 5
```  
Backup interval (seconds)
```
interval = 300
```  
