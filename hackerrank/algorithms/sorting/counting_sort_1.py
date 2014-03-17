# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/countingsort1
'''
__author__ = 'Stas'



if __name__ == '__main__':
    n = input()
    raw = raw_input().split(' ')

    rez_lst = [ 0 for x in xrange(0,100) ]

    for i in raw:
        rez_lst[int(i)] += 1

    print ' '.join([str(x) for x in rez_lst])
