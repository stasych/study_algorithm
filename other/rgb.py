# -*- coding: utf-8 -*-
__author__ = 'stasych'

'''
Задачка из собеседования в Amazone
'''


def div_list_to_3_part(lst):
    R,G,B = 'R','G','B'
    r,b = 0,0
    n = len(lst)

    for i in xrange(0,n/2):
        if lst[i] == R:
            r += 1
        elif lst[i] == B:
            b +=1
        if lst[n-1-i] == R:
            r+=1
        elif lst[n-1-i] == B:
            b+=1
        lst[i] = G
        lst[n-1-i] = G

    for i in xrange(0,n/2):
        if r != 0:
            lst[i] = R
            r -=1
        if b != 0:
            lst[n-1-i] = B
            b -= 1

if __name__ == '__main__':

    print 'case 1: basic. even'
    lst = list('BGBBRRGGBRGB')
    print lst
    div_list_to_3_part(lst)
    print lst

    print 'case 2: basic odd'
    lst = list('BGBBR')
    print lst
    div_list_to_3_part(lst)
    print lst

    print 'case 3: cut'
    lst = list('BR')
    print lst
    div_list_to_3_part(lst)
    print lst

    print 'case 4: one element'
    lst = list('B')
    print lst
    div_list_to_3_part(lst)
    print lst

    print 'case 5: almosr sorted'
    lst = list('GBRRRGGGGBBB')
    print lst
    div_list_to_3_part(lst)
    print lst