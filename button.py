import pygame
from drawInfo import *

class Button:
    def __init__(self, draw_info):
        self.window = draw_info.window
        self.width = draw_info.width
        self.height = draw_info.height
        self.msg = pygame.font.SysFont('arielblack', 70)

    def drawPausedMenu(self, draw_info):

        text = self.msg.render('Paused', True, (0, 0, 0))
        pygame.draw.rect(draw_info.surface, (128, 128, 128, 150), [0, 0, draw_info.width, draw_info.height])
        draw_info.window.blit(draw_info.surface, (0, 0))
        draw_info.window.blit(text, (draw_info.width//2 - 90, draw_info.height//2 - 30))
        pygame.display.update()

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                return self.rect.collidepoint(event.pos)
        return False