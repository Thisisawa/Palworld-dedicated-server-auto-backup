# 帕魯專用伺服器自動備份程式
適用於windows系統的自動備份程式，依照設定時間自動備份遊戲世界檔案，不包含重啟功能  

放置於伺服器根目錄執行即可  
```
py start.py
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
