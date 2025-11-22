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

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center = position)
    return [image, surface, rect]

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    if keys[pygame.K_d]:
        delta_x += speed

    return [delta_x, delta_y]

def limit_position(position):
    x, y = position

    x = max(20, min(x, SCREEN_WIDTH-20))
    y = max(20, min(y, SCREEN_HEIGHT-20))

    return [x, y]

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image("assets/player.png", player_pos)
background_color = [9, 42, 121]

# Kod wykonywany póki aplikacja jest uruchomiona
while game_status:
    # Odczytanie zdarzeń zarejestrowanych przez komputer
    events = pygame.event.get()
    for event in events:
        # Naciśnięto X - zamykanie aplikacji
        if event.type == pygame.QUIT:
            game_status = False

    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)

    player_pos[0] += delta_x
    player_pos[1] += delta_y

    player_pos = limit_position(player_pos)

    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color)
    print_image(player)

    # Odświeżenie wyświetlanego okna
    pygame.display.update()
    clock.tick(60)

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
