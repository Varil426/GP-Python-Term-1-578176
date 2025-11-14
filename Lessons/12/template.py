# Import modułu pygame, dzięki któremu tworzymy aplikacje okienkowa
import pygame

# Zmiana obecnej ścieżki pracy
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Inicjalizacja modułu
pygame.init()

# Utworzenie okna o określonych wymiarach
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Nadanie nazwy oknu
pygame.display.set_caption("Pierwsza Gra")

# Utworzenie zegara, który nadzoruje stałe wartości fps
clock = pygame.time.Clock()

# Zmienna określająca, czy należy zamknąć okno
game_status = True

# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
    for event in events:
        # Naciśnięto X - zamykanie aplikacji
        if event.type == pygame.QUIT:
            game_status = False

    # Odświeżenie wyświetlanego okna
    pygame.display.update()
    clock.tick(60)

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
