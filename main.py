import pygame
from Algorithms.insertionSort import insertionSort
from drawInfo import *

def main():
    pygame.init()
    running = True
    n = 8
    WIDTH, HEIGHT = 800, 600
    draw_info = DrawInfo(WIDTH, HEIGHT)
    pause = True
    CLOCK = pygame.time.Clock()

    while running:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    n = draw_info.n
                    h = draw_info.HEIGHT
                    draw_info.lst = generateList(n, h)

                if event.key == pygame.K_UP:
                    draw_info.n += 1
                    n = draw_info.n
                    h = h = draw_info.HEIGHT
                    draw_info.lst = generateList(n, h)

                if event.key == pygame.K_DOWN:
                    if draw_info.n == 5:
                        draw_info.n = 5
                        # Make note that min sorting values has been reached
                    else:
                        draw_info.n -= 1
                    
                    n = draw_info.n
                    h = h = draw_info.HEIGHT
                    draw_info.lst = generateList(n, h)
                
                if event.key == pygame.K_LEFT:
                    if draw_info.delay == 10:
                        draw_info.delay = 10
                    else:
                        draw_info.delay -= 1

                if event.key == pygame.K_RIGHT:
                    if draw_info.delay == 100:
                        draw_info.delay = 100
                    else:
                        draw_info.delay += 1

                if event.key == pygame.K_SPACE:
                    if not draw_info.paused:
                        draw_info.paused = True
                    else:
                        draw_info.paused = False

        insertionSort(draw_info)
        #draw(draw_info)

    pygame.display.update()

pygame.QUIT

if __name__ == "__main__":
    main()


    # for i in range(n):
    #     for j in range(n - i - 1):
    #         if rects[j][3] > rects[j + 1][3]:
    #             rects[j][3], rects[j + 1][3] = rects[j + 1][3], rects[j][3]
    #             print(rects)
    #             update(rects)