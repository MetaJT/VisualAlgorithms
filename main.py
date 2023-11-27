import pygame
from Algorithms.insertionSort import insertionSort
from drawInfo import *

def main():
    pygame.init()
    running = True
    n = 8
    WIDTH, HEIGHT = 800, 600
    draw_info = DrawInfo(WIDTH, HEIGHT)
    draw_info.algo = insertionSort
    sortingAlgoGenerator = None
    sorting = False
    CLOCK = pygame.time.Clock()
    tick = 25

    while running:
        CLOCK.tick(tick)

        if sorting:
            try:
                next(sortingAlgoGenerator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    n = draw_info.n
                    h = draw_info.HEIGHT
                    draw_info.lst = generateList(n, h)

                if event.key == pygame.K_UP and not sorting:
                    draw_info.n += 1
                    n = draw_info.n
                    h = draw_info.HEIGHT
                    draw_info.lst.append(generateList(n, h)[-1])

                if event.key == pygame.K_DOWN and not sorting:
                    if draw_info.n == 5:
                        draw_info.n = 5
                        # Make note that min sorting values has been reached
                    else:
                        draw_info.n -= 1
                        draw_info.lst.pop()

                if event.key == pygame.K_RIGHT:
                    tick += 5

                if event.key == pygame.K_LEFT:
                    tick -= 5

                if event.key == pygame.K_SPACE:
                    sorting = not sorting
                    sortingAlgoGenerator = draw_info.algo(draw_info)

        #insertionSort(draw_info)
        #draw(draw_info)

    pygame.display.update()

pygame.QUIT

if __name__ == "__main__":
    main()