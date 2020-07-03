echo off
echo [40;37mStart
set ret=1

@echo %1

@rem 4, erase all flash
echo [40;37m
echo Start erase chip ......
nrfjprog --eraseall
if "%errorlevel%"== "0" (
@rem [40;32m
echo Erase chip sucess
) else ( echo [40;31mErase flash fail
goto ERR
)
@rem echo [40;32mErase chip done

echo [40;37m
echo start load hex ......
@rem 5, load hex to flash
nrfjprog --program %1
echo errorlevel=%errorlevel%
if "%errorlevel%"== "0" (
echo [40;32mLoad hex done
@rem nrfjprog --memwr 0x10001080 --val %1
@rem nrfjprog --memrd 0x10001080
goto SUCESS
) else ( 
echo [40;32mLoad hex fail
goto ERR
)

:ERR
echo [40;31mError happen !! Will exit.
set ret=1
@rem pause
goto Exit
@rem exit

:SUCESS
echo [40;32mSuccess! Will exit.
nrfjprog -r
set ret=0
goto Exit
@rem exit

:Exit
@rem echo [40;37m
echo %ret%
exit /b %ret%
