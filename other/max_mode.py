# -*- coding: utf-8 -*-
'''
Дан массив отсортированных целых чисел. Придумать самый
оптимальный алгоритм, который вернет тебе число из массива,
повторяющееся чаще всех остальных.
'''
__author__ = 'Stas'
from collections import defaultdict

def max_mode_unsorded(ar):
    '''
    Если массив чисел не сортированный
    Сложность O(n)
    Память O(n)
    '''
    D = defaultdict(int)
    m = 0
    for x in ar:
        D[x] += 1
        if D[x]>=D[m]:
            m = x
    return m

def max_mode(ar):
    '''
    Если массив чисел отсортирован
    Сложность: O(С)
    Память: O(1)

    по массиву можно двигаться с шагом max_n
    '''
    current_n = 1
    current_index = 1
    current_M = ar[0]

    max_n = 1
    max_M = ar[0]

    while current_index >= len(ar):
        # достингнут элемент >= максимального
        if ar[current_index] == current_M:
            max_n +=1
            max_M = current_M
            current_index += 1
            continue
        # текущий сменился
        else:
            current_M = ar[current_index]
            current_index = current_index +max_n
            for j in range(0,max_n):
                if ar[current_index-j] == current_M:
                    current_index -= 1

    return max_M

if __name__ == '__main__':
    # входной поток чисел через пробел
    ar =  raw_input().strip().split()

    # m = max_mode_unsorded(ar)
    # print 'mode for unsorted array:',m

    M = max_mode(ar)
    print 'mode for sorted array:',M

