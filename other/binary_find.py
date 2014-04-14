# -*- coding: utf-8 -*-
'''
Найти число в отсортированном массиве целых чисел
'''
__author__ = 'Stas'

def binary_search(ar,z):
    '''
    возвращает индекс
    спасибо центру за это
    слова, после дороги начинают приобретать дополнительный смысл
    '''
    rez = None

    if ar[0] == z:
        return 0
    if ar[-1] == z:
        return len(ar)-1

    n = len(ar)
    first = 0
    i = n-1-first+1/2


    while not( i==0 or i == n):
        if ar[i] > z:
            n = i-1
            i = n-1-first+1/2
        elif ar[i]<z:
            first = i+1
            i = n-1-first+1/2
        elif ar[i] == z:
            rez = i
            break
    return rez

if __name__ == '__main__':
    lst = [10,11,12,13,14,15,16,17,18,19,20]

    # case 1: first element
    fisrt = 10
    rez = binary_search(lst,fisrt)
    print 'case 1: first element'
    print 'rez i=',rez,'rez value:',lst[rez]

    # case 2: middle element
    middle = 15
    rez = binary_search(lst,middle)
    print 'case 3: middle element'
    print 'rez i=',rez,'rez value:',lst[rez]

    # case 3: last element
    last = 20
    rez = binary_search(lst,last)
    print 'case 3: last element'
    print 'rez i=',rez,'rez value:',lst[rez]

    # case 4: wrong param

    # case 5: dubles