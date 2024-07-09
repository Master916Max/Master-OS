import os
import multiprocessing
import logging

# Logging setup
logging.basicConfig(level=logging.DEBUG, filename="system-log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("Kernel")

# Adding the same handler and formatter used in Boot.py
handler = logging.FileHandler("F:\\Master1\\log\\kernel.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

def StartUp():
    from System.KP.SFRP import P4, P2

    error, code = P4()
    if code:
        log.error(f"P4 failed: {error}")
        print(error)
        exit()

    error, code = P2()
    if code:
        log.error(f"P2 failed: {error}")
        print(error)
        exit()

    log.info("Startup completed successfully")

def Run():
    log.info("Kernel is running")
