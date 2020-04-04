#!/usr/bin/env python
# coding: utf-8

def wf(x):
    import numpy as np
    import matplotlib.pyplot as plt
    plt.plot(x)
    plt.grid()
    plt.xlim(0,10)
    plt.ylim(-10,10)
    plt.xticks(np.arange(0,11,1))
    plt.yticks(np.arange(-10,11,2))
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

