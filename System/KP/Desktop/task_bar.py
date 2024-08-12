import pygame
import pickle
from multiprocessing import Pipe
import logging

log = logging.getLogger("TaskBar")
handler = logging.FileHandler("F:\\Master\\log\\system.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)

apps = {}

def unpickel(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

class TaskBar:
    def __init__(self):
        self.gdata = unpickel("F:/Master/System/KC/DS.coms")
        self.w = self.gdata[0]
        self.h = self.gdata[1]
        self.taskba = self.st_b()
    def st_b(self):
        self.st_tb= [
            {'type': 'rect', 'color': (100, 100, 100, 182), 'rect': (0, self.h - 50, self.w, 50), "name": "taskbar"}
        ]
        return self.st_tb
    def update(self):
        pass
    def taskbar(self, pipe):
        self.pipe = pipe
        self.update()
        return self.taskba
tk = TaskBar()

def get_taskbar(pipee):
    return tk.taskbar(pipee)