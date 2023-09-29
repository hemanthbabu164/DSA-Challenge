@echo off
for /l %%i in (1, 1, 31) do (
  setlocal enabledelayedexpansion
  set "folder_number=%%i"
  if %%i lss 10 set "folder_number=0%%i"
  set /a "day_sum=18+%%i"
  set "folder_name=!folder_number! - Day!day_sum!"
  mkdir "!folder_name!"
  set "file_name=Day!day_sum!.md"
  copy nul "!folder_name!\!file_name!" >nul
  endlocal
)
