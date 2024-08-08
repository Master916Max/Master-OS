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

save_graphics_data("GM.coms")


from KP.Register import Register

def setup_background(register):
    """Setzt den Hintergrundtyp und die entsprechenden Daten im Register."""
    # Beispielwerte
    background_type = 'color'  # 'color' oder 'image'
    background_value = (0, 0, 255)  # Farbe als (R, G, B) oder Bildpfad

    register.set_entry('System.Grafik.Personalisierung', 'background_type', background_type)
    register.set_entry('System.Grafik.Personalisierung', 'background_value', str(background_value))  # Konvertiere Tuple in String

# Register initialisieren
register_db_path = 'F://Master/System/KC/register.db'
system_register = Register(register_db_path)

# Hintergrund einrichten
setup_background(system_register)
