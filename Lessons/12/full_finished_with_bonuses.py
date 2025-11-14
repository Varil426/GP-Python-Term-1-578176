# Import modulu pygame, dzieki ktoremu tworzymy aplikacje okienkowa
import pygame
from random import choice, randint

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

POINTS_FONT = pygame.font.SysFont("verdana", 20)

bonus_images = ["assets/bonus_1.png", "assets/bonus_2.png", "assets/bonus_3.png"]

FRAMES_PER_SECOND = 60
frames_cnt = 0

# Liczba punktów gracza
player_points = 0


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    # Pozycja wyświetlania obiektu zapisana jest w rect
    rect = surface.get_rect(center=position)

    return [image, surface, rect]


def print_image(img_list) -> None:
    # [image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass


def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]


def calculate_player_movement(keys):
    # Poruszanie postacią
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_d]:
        delta_x += speed
    if keys[pygame.K_a]:
        delta_x -= speed

    return [delta_x, delta_y]


def limit_position(position):
    x, y = position
    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))
    return [x, y]


def generate_bonus_object():
    # Wylosowanie nazwy pliku do wczytania
    image_name = choice(bonus_images)
    # Wylosowanie współrzędnych dla nowego obiektu
    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)
    # Utworzenie zmiennej position, która będzie listą dwuelementową
    position = [x, y]
    # Utworzenie grafiki za pomocą funkcji load_image
    new_obj = load_image(image_name, position)
    # Dodanie gotowego obiektu bonus do listy wszystkich elementów
    bonus_objects.append(new_obj)
    pass


def print_bonus_objects():
    # Iteracja po obiektach bonusowych
    for obj in bonus_objects:
        # Wyświetlenie obiektu na ekranie gry,
        # za pomoca wczesniej przygotowanej funkcji
        print_image(obj)
        pass
    pass


def check_collisions():
    global player_points
    rect_player = player[2]

    # Do wyboru sposób indeksowania
    # for i in range(len(bonus_objects)):
    #    index = len(bonus_objects) - 1 - i
    for index in range(len(bonus_objects) - 1, -1, -1):
        obj = bonus_objects[index]
        rect = obj[2]
        if rect.colliderect(rect_player):
            bonus_objects.pop(index)
            player_points += 1
            print(f"\rPoints: {player_points}", end="")
            pass
        pass
    pass


def print_points(points: int) -> None:
    text = f"Points: {points}"
    color = [255, 255, 255]
    position = [0, 0]
    label = POINTS_FONT.render(text, False, color)
    screen_surface.blit(label, position)
    pass


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image("assets/player.png", player_pos)
background_color = [9, 42, 121]
# Lista przechowująca obiekty bonusowe
# Gotowy obiekt to trójelementowa lista uzyskana z load_image
bonus_objects = []

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
        pass  # for event

    pressed_keys = pygame.key.get_pressed()

    delta_x, delta_y = calculate_player_movement(pressed_keys)

    # Zmiana wartości współrzędnych
    player_pos[0] += delta_x
    player_pos[1] += delta_y
    # Sprawdzenie limitów współrzędnych
    player_pos = limit_position(player_pos)

    # Zmiana współrzędnych obrazu
    player = set_position_image(player, player_pos)

    # Uzupełnij tło
    screen_surface.fill(background_color)
    # Wyświetl gracza
    print_image(player)

    # Dodawanie bonusu - pierwsze dodanie bez warunku ograniczającego ;)
    if frames_cnt % (FRAMES_PER_SECOND * 1) == 0:
        generate_bonus_object()
        pass

    check_collisions()

    print_bonus_objects()

    print_points(player_points)

    # Odświeżenie wyświetlanego okna
    pygame.display.update()

    frames_cnt += 1

    clock.tick(FRAMES_PER_SECOND)
    pass

print("Zamykanie aplikacji")
# Zamknięcie aplikacji
pygame.quit()
# Zamknięcie skryptu
quit()
