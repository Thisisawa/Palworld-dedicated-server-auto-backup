@echo off
if "%1"=="hide" goto CmdBegin
start mshta vbscript:createobject("wscript.shell").run("""%~0"" hide",0)(window.close)&&exit
:CmdBegin
chcp 65001

REM 保存的備份數
set file_count=5
REM 間隔(s)
set interval="300"
REM 備份檔資料夾 
set main_folder="Pal\Saved\SaveGames"
REM "Pal\Saved\SaveGames" === "Pal\Saved\SaveGames\"


set proc="PalServer.exe"

:start
timeout /t 5
tasklist | findstr /i "%proc%"
if errorlevel 1 (
goto :end
)
set YY=%DATE:~4%
set "YY=%YY:/=%"
set hr=%Time:~0,2%
set min=%Time:~3,2%
set sec=%Time:~6,2%
set file_name="%YY%%MM%%DD%%hr%%min%%sec%.zip"
set main_folder="Pal\Saved\SaveGames"
set target_folder="Pal\Saved\SaveGames\0"
set backup_files_folder="Pal\Saved\SaveGames\%file_name%"
PowerShell Compress-Archive -Path "%target_folder%" -DestinationPath "%backup_files_folder%"
echo F|xcopy /Q /Y /F "%main_folder%%file_name%" "%main_folder%\2%file_name%"
del "%main_folder%%file_name%"
for /f "skip=%file_count% delims=" %%A in ('dir /b /o-d /a-d "%main_folder%\*.zip"') do del "%main_folder%\%%A"


timeout /t %interval%
goto :start
:end
echo no server there, good bey
pause