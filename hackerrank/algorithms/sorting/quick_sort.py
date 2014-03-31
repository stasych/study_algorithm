# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/quicksort2
true qsort without memory exceeding
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

def true_partition(ar,l,r):
    v = ar[l]
    i = l+1
    j = r
    while 1:

        while ar[i] > v:
            i +=1
            break

        while ar[j] < v:
            j -= 1
            break

        if i >= j:
            break

        r = ar[i]
        ar[j] = ar[i]
        ar[i] = r



    return i



def true_quicksort(ar):
    if len(ar) == 1:
        return ar[0]

    i = true_partition(ar,0,len(ar)-1)
    true_quicksort(ar[:i-1])
    true_quicksort(ar[i+1:])

    return



if __name__ == '__main__':
    n = input()
    ar = map(int,raw_input().split())

    #rez = quickSort(ar)

    print ' '.join(map(str,ar))
