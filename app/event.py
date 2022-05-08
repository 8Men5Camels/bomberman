import pygame
from abc import ABC, abstractmethod
from app.config import DEFAULT_ENEMY_TIMEOUT, DEFAULT_EFFECT_TIMEOUT
from sprites import CreateEnemy, CreateEffect
from mixins import EngineMixin


class Event(EngineMixin, ABC):
    def __init__(self, ms_timeout):
        super().__init__()
        self.ms_timeout = ms_timeout

    @abstractmethod
    def action(self):
        pass


class AddEnemy(Event):
    def __init__(self, ms_timeout=DEFAULT_ENEMY_TIMEOUT):
        super().__init__(ms_timeout)

        self.event_no = pygame.USEREVENT + 1
        pygame.USEREVENT = self.event_no
        pygame.time.set_timer(self.event_no, self.ms_timeout)
        self.engine.add_event(self)

    def action(self):
        CreateEnemy.spawn_random_enemy()


class AddEffect(Event):
    def __init__(self, ms_timeout=DEFAULT_EFFECT_TIMEOUT):
        super().__init__(ms_timeout)

        self.event_no = pygame.USEREVENT + 1
        pygame.USEREVENT = self.event_no
        pygame.time.set_timer(self.event_no, self.ms_timeout)
        self.engine.add_event(self)

    def action(self):
        CreateEffect.spawn_random_effect()
