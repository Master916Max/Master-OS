import pygame
import pickle

taskbar = [
    {'type': 'rect', 'color': (255, 0, 0), 'rect': (50, 50, 500, 400)},
    {'type': 'rect', 'color': (255, 0, 0), 'rect': (50, 50, 700, 300)}
]

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
        self.taskbar = self.st_b()
    def st_b(self):
        self.st_tb= [
            {'type': 'taskbar', 'color': (100, 100, 100, 128), 'rect': (0, self.h - 50, self.w, 50)}
        ]
        return self.st_tb
tk = TaskBar()

def get_taskbar():
    return tk.taskbar