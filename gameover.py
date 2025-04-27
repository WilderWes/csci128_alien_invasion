import pygame.font
from helpers import draw_text_image

 
class Gameover:
 
    def __init__(self, ai_game):
        """Initialize Gameover Window"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 900, 600
        self.window_color = (0, 0, 0)
        self.text_color = (139, 0, 0)
        self.font_size = 128
        
        # Build the gameover rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once.
        self.msg = "GAMEOVER"


    def draw_window(self):
        # Draw blank window and then draw gameover.
        self.screen.fill(self.window_color, self.rect)
        draw_text_image(self.msg, self.rect.center, self.font_size, self.text_color, self.screen)

        # Continue Message
        playagain_pos = (self.rect.centerx, self.rect.bottom-100)
        draw_text_image(
            text="Press P to play again",
            pos=playagain_pos,
            fontsize=24,
            color=(139, 0, 0),
            screen=self.screen
        )
