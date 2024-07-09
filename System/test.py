import pickle
import pygame
import os

def save_graphics_data(filename):
    
    """Speichert Pygame-Formen in einer Pickle-Datei."""
    shapes = [
        {'type': 'rect', 'color': (255, 0, 0), 'rect': (50, 50, 100, 100)},
        {'type': 'circle', 'color': (0, 255, 0), 'center': (200, 200), 'radius': 50}
    ]
    os.chdir("F://Master/System/KC")
    with open(filename, 'wb') as f:
        pickle.dump(shapes, f)

def load_graphics_data(filename):
    """Lädt Pygame-Formen aus einer Pickle-Datei."""
    with open(filename, 'rb') as f:
        shapes = pickle.load(f)
    return shapes

save_graphics_data("gm.coms")