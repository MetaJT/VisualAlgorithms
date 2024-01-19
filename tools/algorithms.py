from drawInfo import *

# Insertion Sort
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

# Bubble Sort
def bubbleSort(draw_info):
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

# Quick Sort
def quickSort(draw_info):
    lst = draw_info.lst
    n = len(lst)
    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()

        # Partition
        i = (low - 1)
        x = lst[high]
 
        for j in range(low, high):
            if lst[j] <= x:
 
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw(draw_info, i, j)
                yield True
 
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw(draw_info, i + 1, high)
        yield True

        p = i + 1 # partition p

        if p - 1 > low:
            stack.append((low, p - 1))

        if p + 1 < high:
            stack.append((p + 1, high))

# Merge Sort
def mergeSort(draw_info):
    lst = draw_info.lst
    stack = [(0, len(lst) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            mid = (low + high) // 2

            stack.append((mid + 1, high))

            stack.append((low, mid))

            left_half = lst[low:mid + 1]
            right_half = lst[mid + 1:high + 1]

            i = j = 0
            k = low

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    lst[k] = left_half[i]
                    draw(draw_info, k, i)
                    i += 1
                else:
                    lst[k] = right_half[j]
                    draw(draw_info, k, mid + 1 + j)
                    j += 1
                yield True
                k += 1

            while i < len(left_half):
                lst[k] = left_half[i]
                draw(draw_info, k, i)
                yield True
                i += 1
                k += 1


            while j < len(right_half):
                lst[k] = right_half[j]
                draw(draw_info, k, mid + 1 + j)
                yield True
                j += 1
                k += 1
    return lst

DEFAULT_ALGO = bubbleSort
DEFAULT_ALGO_TEXT = "BUBBLE SORT"