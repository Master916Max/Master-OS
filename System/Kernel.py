import multiprocessing
import logging
import time

# Logging setup
logging.basicConfig(level=logging.DEBUG, filename="system-log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
log = logging.getLogger("Kernel")
handler = logging.FileHandler("F:\\Master\\log\\system.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)
# Pipes Creating
def create_pipes(amount) -> list:
    """Erstellt Pipes."""
    pipes = []
    for _ in range(amount):
        pipe_pair = multiprocessing.Pipe()
        pipes.append(pipe_pair)
    return pipes


class PipeManager:
    def __init__(self):
        self.pipes = create_pipes(10)  # Create 10 pipes for communication between the kernel and the other processes
        self.pipe = {}
        self.next_pipe = 0
    def get_pipe(self, name):
        return self.pipe[name]
    
    def set_pipe(self, name):
        self.pipe[name] = self.pipes[self.next_pipe]
        log.debug(f"Pipe: {self.next_pipe} is with: {name} linked")
        self.next_pipe = (self.next_pipe + 1)
        if self.next_pipe > len(self.pipes):
            self.pipes =+ create_pipes(10)
        self.pipe[f"{name}-sys"] = self.pipes[self.next_pipe]
        log.debug(f"Pipe: {self.next_pipe} is with: {name}-sys linked")
        self.next_pipe = (self.next_pipe + 1)
        if self.next_pipe > len(self.pipes):
            self.pipes =+ create_pipes(10)
        return self.pipe[name]




def start_graphics_manager(pm: PipeManager):
    """Startet den Grafikmanager."""
    import System.KP.Desktop.GM as GM
    GM.main(syst_pipe=pm.set_pipe("task_bar"))



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
    log.info("Kernel is running")
    pm = PipeManager()


    graphics_process = multiprocessing.Process(target=start_graphics_manager, args=(pm,))
    graphics_process.start()


    while graphics_process.is_alive():
        time.sleep(1)
    log.critical("Graphics Manager has Crashed")
    

    log.info("Graphics Manager has finished")
    log.info("Kernel is shutting down")

if __name__ == "__main__":
    StartUp()
    Run()
