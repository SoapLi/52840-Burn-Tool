@echo %1
@echo %2
mergehex.exe -m %2 %1 -o %~dp0\nrf52840_withsoftdevice.hex
