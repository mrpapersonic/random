@echo off
echo Downloading pathed...
if not exist %temp%\python3path mkdir %temp%\python3path
if not exist %temp%\python3path\pathed.exe powershell "iwr -OutFile "%temp%\python3path\pathed.exe" https://cdn.discordapp.com/attachments/559034172274901012/795468079432990740/pathed.exe"
if not exist %temp%\python3path\GSharpTools.dll powershell "iwr -OutFile "%temp%\python3path\GSharpTools.dll" https://cdn.discordapp.com/attachments/757237744530358292/795469138469978162/GSharpTools.dll"
if not exist %temp%\python3path\GSharpTools.WPF.dll powershell "iwr -OutFile "%temp%\python3path\GSharpTools.WPF.dll" https://cdn.discordapp.com/attachments/757237744530358292/795469255575076914/GSharpTools.WPF.dll"
if not exist %temp%\python3path\log4net.dll powershell "iwr -OutFile "%temp%\python3path\log4net.dll" https://cdn.discordapp.com/attachments/757237744530358292/795469497141035028/log4net.dll"
%temp%\python3path\pathed.exe /append %userprofile%\AppData\Local\Programs\Python\Python39 /user
%temp%\python3path\pathed.exe /append %userprofile%\AppData\Local\Programs\Python\Python39\Scripts /user
echo Python added to path!
pause
