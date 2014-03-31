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
    '''
    выполняет перестановку в ar[l+1,r], что вначале идут все < ar[l],
    а потом все > ar[l]
    возвращает индекс для ar[l] (pivot)
    '''
    v = ar[l]
    i = l+1
    j = r
    while 1:

        while ar[i] < v:
            i +=1


        while ar[j] > v:
            j -= 1

        if i >= j:
            break

        r = ar[i]
        ar[i] = ar[j]
        ar[j] = r


    ar[l] = ar[i-1]
    ar[i-1] = v

    return i-1



def true_quicksort(ar,l,r):
    '''
    классический квиксорт
    '''
    if len(ar[l:r]) == 1:
        print '*ar[pivot]=',ar[l],'pivot=',l,ar
        return

    i = true_partition(ar,l,r)
    print 'ar[pivot]=',ar[i],'pivot=',i,ar
    true_quicksort(ar,l,i-1)
    print 'go to right',i,l,r
    true_quicksort(ar,i+1,r)

    return



if __name__ == '__main__':
    n = 7
    ar = [5,8,1,3,7,9,2]

    true_quicksort(ar,0,n-1)

    print ' '.join(map(str,ar))
