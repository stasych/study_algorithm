# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/countingsort4
sample successfull passed
INPUT
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

RIGHT OUTPUT
0 ab
0 ef
0 ab
0 ef
0 ij
0 to
1 be
1 or
2 not
2 to
3 be
4 ij
4 that
4 is
4 the
5 question
6 cd
6 gh
6 cd
6 gh
'''
__author__ = 'Stas'

if __name__ == '__main__':
    n = input()
    k = 100
    num_lst = [[] for i in xrange(0,k)]



    for i in xrange(0,n):
        x,s = raw_input().split(' ')
        x = int(x)
        num_lst[x].append(s)


    for x in xrange(0,k):
        for j in num_lst[x]:
            print x,j