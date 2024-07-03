# Desktop Windows Controls System

import os

import pygame

os.chdir("F://Master1")

import pygame
# Classses
class App:
    ...

Apps: {str:App}= {"Test": App()}

class Desktop:
    def __init__(self):
        pygame.init()
        self.desk = pygame.display.set_mode((500, 500), pygame.FULLSCREEN)
        pygame.display.set_caption("Desktop", "F://Master1/System/Icons/Desktop.png")
        while True:
            self.desk.fill(pygame.color.Color(255,255,255))
            pygame.time.delay(10)
Desktop()


class App:
    def __init__(self):
        pass

class TaskListe:
    ...
