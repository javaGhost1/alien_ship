import pygame

class Ship:
    """ Creates the ship and manages it """
    def __init__(self, ai_game):
        """ initialise ship attributes """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # load ship image
        self.image = pygame.image.load('images/download.bmp')
        self.rect = self.image.get_rect()

        # Position the ship
        self.rect.center = self.screen_rect.center
        
        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update ship position """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
        if self.moving_down and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed

    def blitme(self):
        """ Redraw ship current location """
        self.screen.blit(self.image, self.rect)