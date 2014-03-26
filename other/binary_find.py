# -*- coding: utf-8 -*-
'''
Найти число в отсортированном массиве целых чисел
'''
__author__ = 'Stas'

def binary_search(ar,z):
    rez = None
    n = len(ar)-1
    if ar[0] == z:
        return 0
    if ar[-1] == z:
        return len(ar)-1
    i = n/2
    while not( i==0 or i == n):
        print 'i=',i
        if ar[i] > z:
            i = (0+i)/2
        elif ar[i]<z:
            i = (i + n)/2
        elif ar[i] == z:
            rez = i
            break
    return rez

if __name__ == '__main__':
    lst = [10,11,12,13,14,15,16,17,18,19,20]
    z = 17
    rez = binary_search(lst,z)
    print rez,lst[rez]