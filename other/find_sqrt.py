# -*- coding: utf-8 -*-
'''
Найти кол-во квадратов между A <= B. A,B - целые.
'''
__author__ = 'Stas'

def find_root_sqrt(A):
    j = A
    i = A-1

    rez_i = -1
    rez_j = -1

    exclude_digits = [2,3,7,8]

    while True:
        if j%10 in exclude_digits:
            i = A-1
            j += 1
            continue

        if i%10 in exclude_digits:
            i -= 1
            continue

        a = (j-i-1)/2

        if (j-i-1)%2 == 0:
            if i == a*a:
                rez_i = (j-i-1)/2
                rez_j = rez_i+1
                break

        if i == 1:
            i = A-1
            j += 1
            continue

        i -= 1

    return (rez_i,rez_j)


if __name__ == '__main__':
    # Матчасть
    # кол-во квадратов N между b^2 и a^2  N = b-a+1, а также b^2 - a^2 = (N-1)(b+a)
    # если число оканчивается на [2,3,7,8], то это точно не квадрат.
    # то есть x%10 not in [2,3,7,8]
    #
    # возьмем случай A,B не квадраты. Тогда для выч исления N, надо определеить ближайщий квадрат к А и В
    #
    # поиск квадрата рядом с А
    # берется два  числа i = А+1, j = А-1
    # чтобы i=a^2 и j=(а+1)^2 были последовательныи квадратами, необх и достаточно чтобы а = (j-i-1)/2 было целым
    # сдледует из (а+1)^2 - a^2 = 2a+1 = j-i


    A,B = 8,8

    rez_A_l,rez_A_r =  find_root_sqrt(A)
    print rez_A_l,rez_A_r
    rez_B_l,rez_B_r =  find_root_sqrt(B)
    print rez_B_l,rez_B_r

    N = rez_B_r - rez_A_r

    print N