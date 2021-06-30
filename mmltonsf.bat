@echo off

REM - Usage
if "%1" == "" (
    echo usage: compile.bat ^<input^>
    exit /b
)

REM - Compile MML
del /f effect.h
ppmckc.exe -i "%1"
if not exist "effect.h" (
    echo ppmckc ERROR
    exit /b
)

REM - Assemble
del /f ppmck.nes
nesasm -s -raw ppmck.asm
if not exist "ppmck.nes" (
    echo nesasm ERROR
    del /f "%~n1" effect.h define.inc
    exit /b
)

REM - Move files
move /y ppmck.nes "%~n1.nsf"
echo %~n1.nsf written

REM - Cleanup
del /f "%~n1".h effect.h define.inc
