# -*- coding:utf8 -*-
'''
https://github.com/stasych/study_algorithm/issues/11
Вход: функция, которая генерирует случайные числа от 0 до 4
Выход: функция, которая генерирует случайные числа от 0 до 7
'''
__author__ = 'Stas'

import random
from collections import defaultdict

def random_0_4():
    return random.randrange(5)

def random_0_7():
    '''
    use random_0_4 to make random_0_7
    '''
    r1 = random_0_4()
    r2 = random_0_4()
    r = (r1+r2)%8

    return r

def p(f,amount):
    p_dict = defaultdict(int) # распределение
    for x in range(amount):
        n = f()
        p_dict[n] += 1
    return p_dict

if __name__ ==  '__main__':
    N = 100000
    p_0_4 = p(random_0_4,N)
    p_0_7 = p(random_0_7,N)

    for i in range(0,8):
        print 'i:',i,' count:',p_0_4[i]

    print

    for i in range(0,8):
        print 'i:',i,' count:',p_0_7[i]
