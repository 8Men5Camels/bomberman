import pygame
from sprites import Player, Wall
from event import AddEnemy, AddEffect
from engine import Engine
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    DEFAULT_OBJ_SIZE,
    FRAMES_PER_SECOND,
    BACKGROUND_COLOR,
    DEFAULT_ENEMY_TIMEOUT,
    DEFAULT_EFFECT_TIMEOUT,
)


pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

engine = Engine(screen=screen, clock=clock)

player = Player()

engine.player = player

Wall.generate_walls((SCREEN_WIDTH, SCREEN_HEIGHT),
                    (DEFAULT_OBJ_SIZE, DEFAULT_OBJ_SIZE))

add_enemy = AddEnemy(DEFAULT_ENEMY_TIMEOUT)
add_effect = AddEffect(DEFAULT_EFFECT_TIMEOUT)
engine.add_event(add_enemy)
engine.add_event(add_effect)

engine.running = True

while engine.running:

    engine.events_handling()

    engine.groups_update()

    engine.screen.fill(BACKGROUND_COLOR)

    engine.draw_all_sprites()

    engine.draw_interface()

    pygame.display.flip()

    engine.clock.tick(FRAMES_PER_SECOND)

pygame.quit()
