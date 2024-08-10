import pygame
import pickle
import os
import time
from multiprocessing import Pipe
# System Managers
import System.KP.Desktop.task_bar as tb
from System.KP.Desktop.handler import KeyHandler, AppManager


type pipe = None|object
am_pipe = None
sys_pipe = None
apps = []


class Data: 
     def __str__(self) -> str:
        return f"Data()"
def save_screen_resolution(filename):
    """Speichert die aktuelle Bildschirmauflösung in einer Pickle-Datei."""
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    resolution = (screen_width, screen_height)
    
    with open(filename, 'wb') as f:
        pickle.dump(resolution, f)
    print(f"Screen resolution saved: {resolution}")

def load_graphics_data(filename, ame_pipe):
    """Lädt Pickle-Daten von Pygame-Formen."""
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            graphics_data = pickle.load(f)
    else:
        graphics_data = []
    return graphics_data + tb.get_taskbar(ame_pipe)



def main(syst_pipe: pipe = None, ame_pipe: pipe = None):
    apmg = AppManager()
    apmg.start_app("Loading System", 1)
    KH = KeyHandler()
    pygame.init()
    pygame.display.set_caption("MOS Desktop")
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    resolution_file = 'F:/Master/System/KC/DS.coms'
    save_screen_resolution(resolution_file)
    graphics_file = 'F:/Master/System/KC/GM.coms'
    graphics_data = load_graphics_data(graphics_file, ame_pipe)
    close: pygame.Rect = None
    running = True
    while running:
        for event in pygame.event.get():
            KH.app_u(event, apmg.apps)
            running = KH.update(event, close, running)
        graphics_data = load_graphics_data(graphics_file, ame_pipe)
        screen.fill((0, 0, 255))
        for shape in graphics_data:
            if shape['type'] == 'rect':
                if shape["name"] == "close":
                    close = pygame.Rect(*shape['rect'])
                    pygame.draw.rect(screen, shape['color'], close)
                else:
                    pygame.draw.rect(screen, shape['color'], pygame.Rect(*shape['rect']))
            elif shape['type'] == 'circle':
                pygame.draw.circle(screen, shape['color'], shape['center'], shape['radius'])
            elif shape['type'] == 'taskbar':
                task_pos = pygame.Rect(*shape['rect'])
                task_surface = pygame.Surface(task_pos.size, pygame.SRCALPHA)
                pygame.draw.rect(task_surface, shape['color'], task_surface.get_rect())
        # Hier zeichnen wir das App-Element direkt
        apmg.print(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
