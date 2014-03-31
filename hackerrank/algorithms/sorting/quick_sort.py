# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/quicksort2
'''
__author__ = 'Stas'

def partition(ar):
    l = []
    r = []
    p = ar[0]

    for x in ar:
        if x<p:
            l.append(x)
        elif x>p:
            r.append(x)

    return l,r,p

def quickSort(ar):

    if len(ar) == 1:
        return ar


    l,r,p = partition(ar)
    rez = []
    if l:
        rez.extend(quickSort(l))
    rez.append(p)
    if r:
        rez.extend(quickSort(r))
    print ' '.join(map(str,rez))
    return rez



if __name__ == '__main__':
    n = input()
    ar = map(int,raw_input().split())

    #rez = quickSort(ar)

    print ' '.join(map(str,ar))