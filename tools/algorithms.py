from drawInfo import *
import pygame

def insertionSort(draw_info):
    lst = draw_info.lst
    n = len(lst)

    for i in range(n):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]

            draw(draw_info, j)
            j -= 1
            yield True
    return lst