import pygame
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(dimensions)

dvd_logo = pygame.image.load("dvd.png")
dvd_logo = pygame.transform.scale(dvd_logo, (dvd_logo.get_width() // 5, dvd_logo.get_height() // 5))

position = pygame.Vector2(0, 0)
velocity = pygame.Vector2(0.2, 0.1)

clock = pygame.time.Clock()

COLORS = [(0, 0, 255), (255, 0, 255), (255, 0, 0), (255, 128, 0), (255, 255, 255), (255, 255, 0), (0, 255, 0)]

def randomize_logo_color():
    dvd_logo.fill((0, 0, 0), special_flags=pygame.BLEND_MULT)
    dvd_logo.fill(random.choice(COLORS), special_flags=pygame.BLEND_ADD)

def check_edges():
    global velocity
    if (position.y < 0 and velocity.y < 0) or (position.y + dvd_logo.get_height() > SCREEN_HEIGHT and velocity.y > 0):
        velocity.y *= -1
        randomize_logo_color()

    if (position.x < 0 and velocity.x < 0) or (position.x + dvd_logo.get_width() > SCREEN_WIDTH and velocity.x > 0):
        velocity.x *= -1
        randomize_logo_color()

randomize_logo_color()

is_running = True
while is_running:

    screen.fill((0, 0, 0))

    screen.blit(dvd_logo, (position.x, position.y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    position += velocity * clock.get_time()
    check_edges()

    pygame.display.update()
    clock.tick()

pygame.quit()