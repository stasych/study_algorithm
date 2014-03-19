# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/insertionsort1
'''
__author__ = 'Stas'

def sort_last(ar):
    n = len(ar)
    v = ar[n-1]
    print 'Begin sorting...'
    for i in xrange(0,n):
        ar[n-1-i] = ar[n-1-i-1]
        if ar[n-1-i] < v or i==n-1:
            ar[n-1-i] = v
            print ' '.join(map(str,ar))
            break
        print ' '.join(map(str,ar))
    print 'End sorting.'


if __name__ == '__main__':
    s = input()
    ar = [int(i) for i in raw_input().strip().split(' ')]
    sort_last(ar)
    print ' '.join(map(str,ar))
