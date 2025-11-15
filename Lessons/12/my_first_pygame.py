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

def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)

    rect = surface.get_rect(center = position)

    return [image, surface, rect]

def print_image(img_list):
    # [image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image("assets/player.png", player_pos)

# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
    for event in events:
        # Naciśnięto X - zamykanie aplikacji
        if event.type == pygame.QUIT:
            game_status = False

    print_image(player)

    # Odświeżenie wyświetlanego okna
    pygame.display.update()
    clock.tick(60)

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
