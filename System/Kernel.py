import multiprocessing
import logging
from System.KP.Register import Register

# Logging setup
logging.basicConfig(level=logging.DEBUG, filename="system-log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("Kernel")

# Initialize the register
register_db_path = "F://Master/System/KC/register.db"
system_register = Register(register_db_path)

def start_graphics_manager():
    """Startet den Grafikmanager."""
    import System.KP.Desktop.GM as GM
    GM.main()

def StartUp():
    """System-Startroutine."""
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
    """Kernel-Runroutine."""
    log.info("Kernel is running")
    system_register.set_entry("sys_path", "F:\\Master\\", readonly=True)

    # Start the graphics manager as a separate process
    graphics_process = multiprocessing.Process(target=start_graphics_manager)
    graphics_process.start()

    # Wait for the graphics manager to finish
    graphics_process.join()

    log.info("Graphics Manager has finished")
    log.info("Kernel is shutting down")

if __name__ == "__main__":
    StartUp()
    Run()
