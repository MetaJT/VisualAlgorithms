import pygame
from tools.algorithms import *
from drawInfo import *
from button import *

def main():
    pygame.init()
    pygame.font.init()
    running = True
    WIDTH, HEIGHT = 800, 600

    draw_info = DrawInfo(WIDTH, HEIGHT)

    draw_info.algo = mergeSort
    draw_info.algorithm = "MERGE SORT"
    sortingAlgoGenerator = None
    sorting = False
    paused = False # Need to set to true to start
    CLOCK = pygame.time.Clock()
    draw_info.tick = 10
    count = 0
    pauseMenu = Button(draw_info)

    while running:
        tick = draw_info.tick
        CLOCK.tick(tick)

        if sorting and not paused:
            try:
                next(sortingAlgoGenerator)
            except StopIteration:
                sorting = False

        elif not sorting and not paused:
            draw(draw_info)

        elif paused and count != 1:
            pauseMenu.drawPausedMenu(draw_info)
            count = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # Reset sort
                    n = draw_info.n
                    h = draw_info.height
                    draw_info.lst = generateList(n, h)

                if event.key == pygame.K_RIGHT and (not sorting or paused): 
                    draw_info.n += 1
                    n = draw_info.n
                    h = draw_info.height
                    draw_info.lst.append(generateList(n, h)[-1])

                if event.key == pygame.K_LEFT and (not sorting or paused):
                    if draw_info.n == 5:
                        draw_info.n = 5
                        # Make note that min sorting values has been reached
                    else:
                        draw_info.n -= 1
                        draw_info.lst.pop()

                if event.key == pygame.K_UP:
                    draw_info.tick += 5

                if event.key == pygame.K_DOWN:
                    if tick == 5:
                        draw_info.tick = 5
                    else:
                        draw_info.tick -= 5

                if event.key == pygame.K_SPACE:
                    if not sorting:
                        sorting = True
                    else:
                        sorting = not sorting
                    paused = False
                
                if event.key == pygame.K_p:
                    if count == 1:
                        count = 0
                    paused = not paused
                    sorting = True

                if paused:
                    draw(draw_info)
                    pauseMenu.drawPausedMenu(draw_info)

                if event.key == pygame.K_b:
                    draw_info.algo = bubbleSort
                    draw_info.algorithm = "BUBBLE SORT"
                
                if event.key == pygame.K_i:
                    draw_info.algo = insertionSort
                    draw_info.algorithm = "INSERTION SORT"

                if event.key == pygame.K_q:
                    draw_info.algo = quickSort
                    draw_info.algorithm = "QUICK SORT"
                
                sortingAlgoGenerator = draw_info.algo(draw_info)
        pygame.display.update()

pygame.QUIT

if __name__ == "__main__":
    main()
