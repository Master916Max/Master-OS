import logging
import threading
import os
from commanddek import Bcolors
print(f"{Bcolors.BG_BLUE}{Bcolors.LIGHTWHITE}{os.getcwd()}")
logging.basicConfig(level=logging.DEBUG, filename="system-log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("System")
handler = logging.FileHandler("F:\\Master1\\log\\system.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
log.debug("System is seting up")
def main_system():
    log.info("System is Starting")
    os.chdir(f"F://Master1")
    def start():
        import System.Kernel as KE
        KE.StartUp()
        log.info("System is Running")
        KE.Run()
        log.info("System was Shutdown")
    threading.Thread(target=start).start()



if __name__ == "__main__":
    main_system()

