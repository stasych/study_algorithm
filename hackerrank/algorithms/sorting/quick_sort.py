# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/quicksort2
'''
__author__ = 'Stas'

def partition(ar):
    l = []
    r = []

    for x in ar:
        if x<ar[0]:
            l.append(x)
        else:
            r.append(x)
    l.extend(r)
    print ' '.join(map(str,l))

if __name__ == '__main__':
    n = input()
    ar = map(int,raw_input().split())

    partition(ar)

