#!/usr/bin/env python
# coding: utf-8

def wf(x):
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline
    plt.rcParams['figure.figsize'] = [15, 5]
    plt.plot(x)
    plt.grid()
    plt.xlim(0,20)
    plt.ylim(-5,5)
    plt.xticks(np.arange(0,31,1))
    plt.yticks(np.arange(-5,6,1))
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()