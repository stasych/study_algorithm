# -*- coding: utf-8 -*-
__author__ = 'Stas'

def sort_last(ar):
    n = len(ar)
    v = ar[n-1]
    for i in xrange(1,n):
        if ar[n-1-i] >= v:
            ar[n-1-i+1] = ar[n-1-i]
            print ' '.join(map(str,ar))
        else:
            ar[n-1-i+1] = v
            print ' '.join(map(str,ar))
            break


if __name__ == '__main__':
    s = input()
    ar = [int(i) for i in raw_input().strip().split(' ')]
    sort_last(ar)
