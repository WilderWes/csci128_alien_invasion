import pygame

def draw_text_image(text, pos, fontsize, color, screen):
    font = pygame.font.SysFont(None, fontsize)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = pos
    screen.blit(text_image, text_rect)

