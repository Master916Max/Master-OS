import logging
import os
import multiprocessing
from commanddek import Bcolors



print(f"{Bcolors.BG_BLUE}{Bcolors.LIGHTWHITE}{os.getcwd()}{Bcolors.ENDC}")
logging.basicConfig(level=logging.DEBUG, filename="system-log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("Boot")
handler = logging.FileHandler("F:\\Master\\log\\system.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

def start_kernel():
    import System.Kernel as KE
    KE.StartUp()
    import System.test
    log.info("Kernel is Starting")
    KE.Run()
    log.info("Kernel was Shutdown")

def main_system(log):
    log.info("System is Starting")
    os.chdir("F://Master")

    kernel_process = multiprocessing.Process(target=start_kernel)
    kernel_process.start()

    kernel_process.join()

if __name__ == "__main__":
    main_system(log)
