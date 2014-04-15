# -*- coding: utf8 -*-
__author__ = 'stasych'

def recursion_cicle(n,k):
    print 'recursion state',n
    return n*1.0  if n==k else recursion_cicle(n-1,k)

if __name__ == '__main__':
    # change cicle to recurtion
    # print n*1.0 when n==k

    n = 37
    k = 31

    rez = recursion_cicle(n,k)
    print 'result', rez
