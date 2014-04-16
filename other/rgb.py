# -*- coding:utf8 -*-
__author__ = 'stasych'

'''
Задачка из собеседования в Amazone
'''

if __name__ == '__main__':
    data = 'BGBBRRGGBRGB'
    lst = list(data)
    print lst
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

    print lst