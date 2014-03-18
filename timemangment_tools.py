# -*- coding: utf-8 -*-
__author__ = 'Stas'
import time
import winsound
from collections import namedtuple

if __name__ == '__main__':
    timer_period = 60*30

    Note = namedtuple('Note',['freq','dur'])

    E = Note(freq=660,dur=500)
    G = Note(freq=785,dur=500)
    A= Note(freq=880,dur=1000)

    A_dies= Note(freq=932,dur=300)


    while 1:
        winsound.Beep(E.freq,E.dur)
        winsound.Beep(G.freq,G.dur)
        winsound.Beep(A.freq,A.dur)

        winsound.Beep(E.freq,E.dur)
        winsound.Beep(G.freq,G.dur)
        winsound.Beep(A_dies.freq,A_dies.dur)
        winsound.Beep(A.freq,A.dur)

        winsound.Beep(E.freq,E.dur)
        winsound.Beep(G.freq,G.dur)
        winsound.Beep(A.freq,A.dur)
        winsound.Beep(G.freq,G.dur)
        winsound.Beep(E.freq,A.dur)

        time.sleep(timer_period)