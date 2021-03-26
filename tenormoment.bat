@if [%1] == [] goto usage
@if not exist "%1" goto usage
@if not "%2" == "--debug" @echo off
setlocal enabledelayedexpansion
set "time=0"
:question
if not exist "%~n1" goto start
set /p "answer=The folder '%~n1' already exists. Would you like to overwrite or merge the contents? [o/m]: "
if "%answer%" == "o" (
	del /f /s /q "%~n1"
	goto start
)
if "%answer%" == "m" goto start
goto question


:start
if not exist "%~n1" mkdir "%~n1"
ffmpeg -i "%1" -y -t 5 -ss %time% -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 "%~n1\gif_%time%.gif"
for /F "tokens=*" %%F in ("%~n1\gif_%time%.gif") do set "size=%~z1"
echo %~z1 and !size!
if "!size!" == "0" (
	del "%~n1\gif_%time%.gif"
	exit /B
)
set /a "time=%time%+5"
goto start

:usage
echo usage: %0 ^<video^>
