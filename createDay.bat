@echo off 
set /p date=Enter Day (with leading 0 if smaller 10): 
set day=day%date%
if not exist %day% (mkdir %day%) else (exit /b 0)
cp day00\day00.py %day%\%day%.py
cp day00\main.cpp %day%\main.cpp
cp day00\data.txt %day%\data.txt
cp day00\data.txt %day%\testdata.txt
(Get-Content %day%\%day%.py) -replace 'day00', '%day%' | Out-File -encoding ASCII %day%\%day%.py
exit /b 0