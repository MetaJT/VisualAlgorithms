from drawInfo import *

# Insertion Sort
def insertionSort(draw_info):
    draw_info.ALGORITHM = "INSERTION SORT"
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

# Bubble Sort
def bubbleSort(draw_info):
    draw_info.ALGORITHM = "BUBBLE SORT"
    lst = draw_info.lst
    n = len(lst)
    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw(draw_info, j, j + 1)
                yield True
        if not swapped:
            return