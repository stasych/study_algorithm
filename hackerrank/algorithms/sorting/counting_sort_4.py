# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/countingsort4
'''
__author__ = 'Stas'

if __name__ == '__main__':
    n = input()
    num_lst = []
    txt_lst = []

    from collections import defaultdict
    data = defaultdict(int)

    for i in xrange(0,n):
        x,s = raw_input().split(' ')
        num_lst.append(int(x))
        txt_lst.append(s)

        data[int(x)] += 1

    cur_summ = data[0]
    output = ''+str(cur_summ)
    for x in xrange(1,100):
        cur_summ += data[x]
        appendings = ' '+str(cur_summ)
        output += appendings

    print output

