# -*- coding: utf-8 -*-
'''
Найти число в отсортированном массиве целых чисел
'''
__author__ = 'Stas'

def binary_search(ar,z):
    '''
    возвращает индекс
    спасибо центру за это
    слова, после дороги начинают приобретать дополнительный смысл
    '''
    rez = None

    n = len(ar)-1
    first = 0

    # n-first+1 - количество элементов
    i = first + (n-first+1)/2 - 1 if (n-first+1)%2 == 0 else first + (n-first+1)/2

    while not( i== first or i==n ):
        if ar[i] == z:
            rez = i
            break

        if ar[i] > z:
            n = i-1
        else:
            first = i+1

        i = first+(n-first+1)/2 - 1 if (n-first+1)%2 == 0 else first + (n-first+1)/2

    if ar[first] == z:
        return first
    if ar[n] == z:
        return n

    return rez

def recursive_binary_search(ar,i,n,z):
    # steb by step one-olliner
    # base: return index
    # return 0 if 1 else recursive_binary_search(ar,i+0,n+0,z)
    # end of finding recursion: a[middle]==z
    # return -1 if ar[-1]==z else recursive_binary_search(ar,i+0,n+0,z)
    # if end of divition: n==i(end)
    # return -1 if ar[-1]==z else recursive_binary_search(ar,n+0,i,z)  if i!=n else None
    # determine middle. number of elements=(n-i+1). minddle = i+(n-i+1)/2 - 1 if (n-i+1)%==2 else (n-i+1)/2
    # return i+(n-i+1)/2-1 if (n-i+1)%2==0 else i+(n-i+1)/2 if ar[i+(n-i+1)/2-1 if (n-i+1)%2==0 else i+(n-i+1)/2]==z else recursive_binary_search(ar,i+0,n+0,z) if i!=n else None
    # determine i and n, if ar[middle]>z then n=middle-1, else i=middle+1
    # print 'debug i=',i,'n=',n
    # print 'debug middle=', i+(n-i+1)/2-1 if (n-i+1)%2==0 else i+(n-i+1)/2,'ar[middle]=',ar[i+(n-i+1)/2-1 if (n-i+1)%2==0 else i+(n-i+1)/2]
    return (i+(n-i+1)/2-1 if (n-i+1)%2==0 else i+(n-i+1)/2) if ar[(i+(n-i+1)/2-1) if (n-i+1)%2==0 else i+(n-i+1)/2]==z else (recursive_binary_search(ar,i,(-1+i+(n-i+1)/2-1) if (n-i+1)%2==0 else -1+i+(n-i+1)/2,z) if ar[(i+(n-i+1)/2-1) if (n-i+1)%2==0 else i+(n-i+1)/2]>z else recursive_binary_search(ar,(1+i+(n-i+1)/2-1) if (n-i+1)%2==0 else 1+i+(n-i+1)/2,n,z) )


if __name__ == '__main__':
    lst = [10,11,12,13,14,15,16,17,18,19,20]

    # case 1: first element
    fisrt = 10
    rez = binary_search(lst,fisrt)
    print 'case 1: first element'
    print 'rez i=',rez,'rez value:',lst[rez]
    print

    # case 2: middle element
    middle = 15
    rez = binary_search(lst,middle)
    print 'case 3: middle element'
    print 'rez i=',rez,'rez value:',lst[rez]
    print

    # case 3: last element
    last = 20
    rez = binary_search(lst,last)
    print 'case 3: last element'
    print 'rez i=',rez,'rez value:',lst[rez]
    print

    # case 4: wrong param
    wrong = 11
    rez = binary_search(lst,wrong)
    print 'case 4: worng element'
    print 'rez i=',rez
    print

    # case 5: dubles
    dbl_lst = [10,11,11,12,13,14,15,15,16,17,18,20]
    dbl_element = 11
    rez = binary_search(dbl_lst,dbl_element)
    print 'case 5: dbl element'
    print 'rez i=',rez,'rez value',dbl_lst[rez]
    print

    # case 6: recurse oneliner
    recurse_test = 18
    rez = recursive_binary_search(lst,0,len(lst)-1,recurse_test)
    print 'case 6: recurse'
    print 'rez i=',rez,'rez value:',lst[rez]
    print