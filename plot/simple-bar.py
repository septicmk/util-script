import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

""" input:
data = np.array([[2439.45, 164.634765],
                 [50.5063, 52.421669],
                 [56.4439, 14.584431]])
"""
def draw_bar(ax, data):
    w = 0.25;
    x = np.array([0, 1])
    xname = ["Grape", "DGL"]
    ax.bar(x-w, data[0], w, label="IO", lw=1, edgecolor='k', color='k', hatch='+')
    ax.bar(x, data[1], w, label="Serialization", edgecolor='k', color=ycmap[1])
    ax.bar(x+w, data[2], w, label ="Deserialization", edgecolor='k', color='white', hatch='\\')
    ax.set_yscale('log')
    ax.set_ylabel('Runtime (s)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    ax.legend(prop={'size': 6})
