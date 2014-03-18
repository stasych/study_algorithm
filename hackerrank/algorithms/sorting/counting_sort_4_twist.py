# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/countingsort4
The Twist
'''
__author__ = 'Stas'

if __name__ == '__main__':
    n = input()
    k = 100
    num_lst = [[] for i in xrange(0,k)]

    for i in xrange(0,n):
        x,s = raw_input().split(' ')
        x = int(x)
        if i < n/2:
            num_lst[x].append('-')
        else:
            num_lst[x].append(s)

    output = ''
    for x in xrange(0,k):
        for j in num_lst[x]:
            output += j+' '
    print output[:-1]