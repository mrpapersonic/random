@echo off
REM - file checks
if [%1] == [] echo usage: %0 ^<video^>
if not exist %1 echo usage: %0 ^<video^>
setlocal enabledelayedexpansion
set "time=0"

REM - folder checks
:question
if not exist "%~n1" goto start
set /p "answer=The folder '%~n1' already exists. Would you like to overwrite or merge the contents? [o/m]: "
if "%answer%" == "o" (
	del /f /s /q "%~n1"
	goto start
)
if "%answer%" == "m" goto start
goto question

REM - 
:start
if not exist "%~n1" mkdir "%~n1"
ffmpeg -i %1 -y -t 5 -ss %time% -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 "%~n1\gif_%time%.gif"
for /F "tokens=*" %%F in ("%~n1\gif_%time%.gif") do set "size=%%~zF"
if "!size!" == "0" (
	del "%~n1\gif_%time%.gif"
	exit /B
)
set /a "time=%time%+5"
goto start
