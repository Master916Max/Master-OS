import pygame

# Pygame initialisieren
pygame.init()

# Fenstergröße festlegen
screen = pygame.display.set_mode((800, 600))

# Farbe definieren (Rot) mit Alpha-Wert (128 für halbtransparent)
rect_color = (255, 0, 0, 255)  # (R, G, B, Alpha)

# Rechteckgröße und Position definieren
rect_position = pygame.Rect(100, 100, 300, 200)

# Erstelle eine Oberfläche mit einem Alpha-Kanal (transparente Fläche)
rect_surface = pygame.Surface(rect_position.size, pygame.SRCALPHA)

# Rechteck auf der Oberfläche zeichnen
pygame.draw.rect(rect_surface, rect_color, rect_surface.get_rect())

# Haupt-Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bildschirm mit einer Farbe füllen (z.B. Schwarz)
    screen.fill((0, 0, 0))

    # Zeichne das halbtransparente Rechteck auf den Bildschirm
    screen.blit(rect_surface, rect_position.topleft)

    # Aktualisiere den Bildschirm
    pygame.display.flip()

# Pygame beenden
pygame.quit()
