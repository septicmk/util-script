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

def draw_stack_bar(_ax, ax):
    base =   np.array(
            [[24.947917, 9.86953125],
             [22.720545, 40.9888]]).T
    plasma=np.array(
            [[15.401334, 0.000187],
             [16.796730, 0.804495]]).T
    over = np.array([0, 22.720545+140.9888])
    width = 0.35
    names = ["tensor", "dataframe"]
    cmaps = [ycmap[1], ycmap[0]]
    lbl = ["Store", "Load"]
    x = np.array([0, 1])
    xname = ["FS", "Alluxio"]
    ax.bar(x-width/2, base[0], width, color=cmaps[0], lw=1, edgecolor='k', label = lbl[0])
    ax.bar(x+width/2, plasma[0], width, color=cmaps[0], lw=1, edgecolor='k',)

    ax.bar(x-width/2, base[1], width, bottom=base[0], color=cmaps[1], lw=1, edgecolor='k', label = lbl[1])
    ax.bar(x+width/2, plasma[1], width, bottom=plasma[0], color=cmaps[1], lw=1, edgecolor='k')

    _ax.bar(x-width/2, over, width, color=cmaps[1], lw=1, edgecolor='k', label = lbl[0])
    _ax.bar(x+width/2, [0,0], width, color=cmaps[0],lw=1, edgecolor='k', label=lbl[1])
    #_ax.get_xaxis().set_visible(False)
    _ax.set_xticklabels([])
    for tic in _ax.xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
        tic.tick1line.set_visible(False)
        tic.tick2line.set_visible(False)
        tic.label1.set_visible(False)
        tic.label2.set_visible(False)

    ax.set_ylabel('Runtime (s)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    _ax.grid(ls='--')
    ax.set_axisbelow(True)
    _ax.set_axisbelow(True)
    ax.set_ylim(0,22.720545+40.0888)
    _ax.set_ylim(100, 22.720545+140.9888+20)
    _ax.legend(prop={'size': 6})
    # ax.set_yscale('log')


