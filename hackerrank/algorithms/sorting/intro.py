# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/challenges/tutorial-intro
'''
__author__ = 'Stas'

if __name__ == '__main__':
    v = input()
    n = input()

    for i,c in enumerate(raw_input().split(' ')):
        if c == str(v):
            print i