@echo off

rem This script is part of the TexMaths package
rem http://roland65.free.fr/texmaths
rem
rem Roland Baudin (roland65@free.fr)

rem Convert URL to path 
setlocal enabledelayedexpansion
set fontpath=%1
set fontpath=%fontpath:~8%
set fontpath=!fontpath:%%20= !
set fontpath="%fontpath:/=\%"

rem Font file names
set filename1=TexMaths-Symbols.ttf
set filename2=TexMaths-BB.ttf
set filename3=TexMaths-Cal.ttf
set filename4=TexMaths-Frak.ttf
set filename5=TexMaths-Scr.ttf
set filename6=TexMaths-Rm.ttf

rem Font names
set fontname1=TexMaths Symbols
set fontname2=TexMaths BlackBoard
set fontname3=TexMaths Calligraphic
set fontname4=TexMaths Fraktur
set fontname5=TexMaths Script
set fontname6=TexMaths Roman

rem Delete registry key
reg delete "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /f

rem Copy font files to user local fonts directory
copy %fontpath%%filename1% "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts"
copy %fontpath%%filename2% "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts"
copy %fontpath%%filename3% "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts"
copy %fontpath%%filename4% "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts"
copy %fontpath%%filename5% "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts"
copy %fontpath%%filename6% "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts"

rem Install fonts
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%fontname1% (TrueType)" /t REG_SZ /d "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts\%filename1%" /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%fontname2% (TrueType)" /t REG_SZ /d "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts\%filename2%" /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%fontname3% (TrueType)" /t REG_SZ /d "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts\%filename3%" /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%fontname4% (TrueType)" /t REG_SZ /d "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts\%filename4%" /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%fontname5% (TrueType)" /t REG_SZ /d "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts\%filename5%" /f
reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "%fontname6% (TrueType)" /t REG_SZ /d "C:\Users\%username%\AppData\Local\Microsoft\Windows\Fonts\%filename6%" /f
