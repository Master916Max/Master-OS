import pygame
import pickle
import os
# System Managers
import task_bar as tb
# import apps as app
# import person

def save_screen_resolution(filename):
    """Speichert die aktuelle Bildschirmauflösung in einer Pickle-Datei."""
    screen_width = pygame.display.Info().current_w
    screen_height = pygame.display.Info().current_h
    resolution = (screen_width, screen_height)
    
    with open(filename, 'wb') as f:
        pickle.dump(resolution, f)
    print(f"Screen resolution saved: {resolution}")

def load_graphics_data(filename):
    """Lädt Pickle-Daten von Pygame-Formen."""
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            graphics_data = pickle.load(f)
    else:
        graphics_data = []
    return graphics_data + tb.get_taskbar()

def main():
    # Initialisiere Pygame
    pygame.init()

    # Erhalte aktuelle Bildschirmauflösung
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h

    # Setze Pygame-Fenster auf Vollbildmodus
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Speichere Bildschirmauflösung
    resolution_file = 'F:/Master/System/KC/DS.coms'
    save_screen_resolution(resolution_file)

    # Lade anfängliche Grafikdaten
    graphics_file = 'F:/Master/System/KC/GM.coms'
    graphics_data = load_graphics_data(graphics_file)

    # Haupt-Render-Schleife
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Lade die Grafikdaten kontinuierlich
        graphics_data = load_graphics_data(graphics_file)
        
        # Fülle den Bildschirm mit Hintergrundfarbe (schwarz)
        screen.fill((0, 0, 255))
        
        # Zeichne die Formen aus den Grafikdaten
        for shape in graphics_data:
            if shape['type'] == 'rect':
                pygame.draw.rect(screen, shape['color'], pygame.Rect(*shape['rect']))
            elif shape['type'] == 'circle':
                pygame.draw.circle(screen, shape['color'], shape['center'], shape['radius'])
            elif shape['type'] == 'taskbar':
                pygame.draw.rect(screen, shape['color'], pygame.Rect(*shape['rect']))
        
        # Aktualisiere den Bildschirm
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
