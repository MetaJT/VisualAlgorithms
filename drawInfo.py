import random
import pygame

class DrawInfo:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = BLACK

    def __init__(self,WIDTH,HEIGHT,ALGO=None,N=50, COLOR=GREY,PAUSED=False):
        self.width = WIDTH
        self.height = HEIGHT
        self.n = N
        self.color = COLOR
        self.lst = generateList(N, HEIGHT)
        self.algo = ALGO

        self.window = pygame.display.set_mode([WIDTH,HEIGHT])
        self.surface = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        pygame.display.set_caption("Sorting Algos")

def generateList(n, height):
    lst = []
    for _ in range(n):
        rand = random.randrange(height)
        lst.append(rand)
    return lst

def draw(draw_info, swap1=-1, swap2=0):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR) # clear the screen
    drawList(draw_info, swap1, swap2)

def drawList(draw_info, swap1, swap2=0):
    lst = draw_info.lst
    size = len(lst)
    blockW = draw_info.width / size

    for i, value in enumerate(lst):
        x  = i * blockW
        y = draw_info.height - value

        if i == swap1:
            color = draw_info.GREEN
        elif i == swap2 and swap2 != 0:
            color = draw_info.RED
        else:
            color = draw_info.GREY

        pygame.draw.rect(draw_info.window, color, (x,y, blockW - 1, value))
