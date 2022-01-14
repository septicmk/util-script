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
    #ax.set_axisbelow(True)
    #ax.legend(prop={'size': 6})

def draw_bar(ax, data):
    lbl = ["default", "optimal"]
    cmaps = ["k", "tan"]
    new_path="./new_%s.etl" % (app)
    old_path="./old_%s.etl" % (app)
    #dft = np.loadtxt(old_path).T
    #opt = np.loadtxt(new_path).T
    opt = opt/dft
    dft = dft/dft
    mask = np.ones(15, dtype=bool)
    mask[[2,4,6,8,9]] = False
    opt = opt[mask]
    dft = dft[mask]
    print(opt)
    width=0.35
    #plt.get_cmap('gray')(np.linspace(0.15, 0.85, 3))
    #ax.xaxis.set_visible(False)
    #ax.yaxis.set_visible(False)
    x = np.arange(len(names))
    rect=ax.bar(x-width/2, dft, width, color=cmaps[0], lw=1, edgecolor='k', label=lbl[0], hatch='+')
    rect=ax.bar(x+width/2, opt, width, color=cmaps[1], lw=1, edgecolor='k', label=lbl[1], hatch='//')
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.grid(axis='y', ls='--')
    #ax.set_yscale('log')
    #ax.set_xlim(0, np.sum(data, axis=1).max())
    #ax.set_ylim(-0.4, 7.4)

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


