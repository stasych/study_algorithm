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
    '''
    равномерно распределена
    '''
    return random.randrange(5)

def random_0_7():
    '''
    use random_0_4 to make random_0_7
    '''
    r1 = random_0_4()
    r2 = random_0_4()
    r = (r1+r2)%8

    return r

def random_0_7_new(last_appearance_num_lst=[-1,]):
    '''
    Использую трюк с хранением внутреннего состояния
    '''

    new_rand = random_0_4()
    last_appearance_num_lst[0] = random_0_4()

    if last_appearance_num_lst[0] == 4:
        last_appearance_num_lst[0] = random_0_4()
        return 5
    if last_appearance_num_lst[0] == 3:
        last_appearance_num_lst[0] = random_0_4()
        return 6
    if last_appearance_num_lst[0] == 2:
        last_appearance_num_lst[0] = random_0_4()
        return 7
    # if last_appearance_num_lst[0] == 1:
    #     last_appearance_num_lst[0] = random_0_4()
    #     pass
    # if last_appearance_num_lst[0] == 0:
    #     last_appearance_num_lst[0] = random_0_4()
    #     pass


    return new_rand



def p(f,amount):
    '''
    Отображет распределение функции
    '''
    p_dict = defaultdict(int) # словать для подсчета распределения чисел
    for x in range(amount):
        n = f()
        p_dict[n] += 1
    return p_dict

if __name__ ==  '__main__':
    N = 10000
    p_0_7 = p(random_0_7,N)
    p_0_7_new_tst = p(random_0_7_new,N)

    # expected result for p_0_7
    print 'case 1: brute force'
    for i in range(0,9):
        print 'i:',i,' count:',p_0_7[i]

    print

    # expected result for p_0_7_new_tst
    print 'case 2: new algorytm'
    for i in range(0,8):
        print 'i:',i,' count:',p_0_7_new_tst[i]
