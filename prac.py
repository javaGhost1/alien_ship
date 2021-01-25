import pygame
import sys

from settings import Settings
from ship import Ship

class AlienNation:
    """ Creates an alein game """
    def __init__(self):
        """ initialise the game and run it """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Nation")
        self.ship = Ship(self)
    
    def run_game(self):
        while True:
            self.check_updates()
            self.ship.update()
            self.update_screen()
            

    def check_updates(self):
        """ Updates """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Check for key presses """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_up = True
        if event.key == pygame.K_UP:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ check for key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_up = False
        if event.key == pygame.K_UP:
            self.ship.moving_down = False

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    ai = AlienNation()
    ai.run_game()