# -*- coding:utf8 -*-
__author__ = 'Stas'

def tst_unmutable_param(item, stuff = []):
    '''
    if default value is unmutable, then function rewrite default value each function call
    '''
    stuff.append(item)
    print stuff

def tst_mutable_param(item, state=0):
    '''
    if default value is unmutable, then function rewrite default value each function call
    '''
    state = state
    print state

if __name__ == '__main__':
    tst_unmutable_param(1)
    tst_unmutable_param(2)
    tst_unmutable_param(3)

    tst_mutable_param(1)
    tst_mutable_param(2)
    tst_mutable_param(3)