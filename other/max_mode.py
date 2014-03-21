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
    Сложность: O(n)
    Память: O(1)
    '''
    current_M = ar[0]
    current_n = 0

    max_n = 0
    max_M = ar[0]

    for x in ar:
        if x == current_M:
            current_n += 1
        else:
            if max_n <= current_n:
                # x сменилось
                max_n = current_n
                max_M = current_M

            #обнуляем
            current_n = 1
            current_M = x

    # для последнего элемента
    if max_n < current_n:
        current_n = current_n
        max_M = current_M

    return max_M

if __name__ == '__main__':
    # входной поток чисел через пробел
    ar =  raw_input().strip().split()

    # m = max_mode_unsorded(ar)
    # print 'mode for unsorted array:',m

    M = max_mode(ar)
    print 'mode for sorted array:',M

