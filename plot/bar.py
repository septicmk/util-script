import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

# draw single group bar
# colors = ["k", "dimgray", "gray", "lightgray", "w", "r"]
# labels = ["ORD+ORD", "ORD+ORDf", "ORDf+ORD", "ORDf+ORDf", "Alluxio"]
# labels = colros
def draw_barh0(ax, xname, data, labels, colors):
    x = np.array(range(len(xname)))
    rect=ax.barh(x, data, 0.6, color=colors, lw=1, edgecolor='k', label=labels)
    ax.invert_xaxis()
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(True)
    #ax.set_xscale('log')

""" input:
data = np.array([[2439.45, 164.634765],
                 [50.5063, 52.421669],
                 [56.4439, 14.584431]])
"""
def draw_bar(ax, xname, data, labels, colors, hatchs):
    w = 0.25;
    x = np.array(range(len(xname)))
    ax.bar(x-w, data[0], w, label=labels[0], lw=1, edgecolor='k',  color=colors[0], hatch=hatchs[0])
    ax.bar(x,   data[1], w, label=labels[1], lw=1, edgecolor='k',  color=colors[1])
    ax.bar(x+w, data[2], w, label =labels[2],lw=1, edgecolor='k',  color=colors[2], hatch=hatchs[2])
    ax.set_yscale('log')
    ax.set_ylabel('Runtime (s)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.legend(prop={'size': 6})

#label = ["comp", "overhead"]
#xname = ["co-location", "replication", "evivtion"]
def draw_stack_bar(ax, xname, data, labels, colors):
    #cmaps = [ycmap[1], ycmap[0]]
    #x = np.array([0.2, 1, 1.8])
    x = np.array(range(len(xname)))
    width = 0.35
    ax.bar(x, data[0], width,              color=cmaps[0], lw=1, edgecolor='k', label = lbl[0])
    ax.bar(x, data[1], width, bottom=comp, color=cmaps[1], lw=1, edgecolor='k', label = lbl[1])

    #_ax.get_xaxis().set_visible(False)
    ax.set_ylabel('Runtime (s)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    ax.set_ylim(0,110)
    ax.legend(prop={'size': 10})
    # ax.set_yscale('log')

# drao stack bars on two axis.
def draw_stack_bar(axs, xname, data, labels, colors):
    #over = np.array([0, 22.720545+140.9888])
    width = 0.35
    names = ["tensor", "dataframe"]
    cmaps = [ycmap[1], ycmap[0]]
    lbl = ["Store", "Load"]
    x = np.array([0, 1])
    xname = ["FS", "Alluxio"]
    ax[0].bar(x-width/2, data[0], width, color=colors[0], lw=1, edgecolor='k', label = labels[0])
    ax[0].bar(x+width/2, data[1], width, color=colors[0], lw=1, edgecolor='k', label = labels[1])

    ax[0].bar(x-width/2, data[0], width, bottom=data[0], color=colors[1], lw=1, edgecolor='k', label = labels[1])
    ax[0].bar(x+width/2, data[1], width, bottom=data[1], color=colors[1], lw=1, edgecolor='k', label = labels[1])

    ax[1].bar(x-width/2, over, width, color=colors[1], lw=1, edgecolor='k', label = labels[0])
    ax[1].bar(x+width/2, [0,0], width, color=colors[0],lw=1, edgecolor='k', label = labels[1])
    #_ax.get_xaxis().set_visible(False)
    ax[1].set_xticklabels([])
    for tic in ax[1].xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False
        tic.tick1line.set_visible(False)
        tic.tick2line.set_visible(False)
        tic.label1.set_visible(False)
        tic.label2.set_visible(False)

    ax[0].set_ylabel('Runtime (s)')
    ax[0].set_xticks(x)
    ax[0].set_xticklabels(xname)
    ax[0].grid(ls='--')
    ax[1].grid(ls='--')
    ax[0].set_axisbelow(True)
    ax[1].set_axisbelow(True)
    ax[0].set_ylim(0, 22.720545+40.0888)
    ax[1].set_ylim(100, 22.720545+140.9888+20)
    ax[1].legend(prop={'size': 6})
    # ax.set_yscale('log')

def draw_bar(ax, xname, data, labels, colors):
    mask = np.ones(15, dtype=bool)
    mask[[2,4,6,8,9]] = False
    opt = opt[mask]
    dft = dft[mask]
    print(opt)
    width=0.35
    #plt.get_cmap('gray')(np.linspace(0.15, 0.85, 3))
    #ax.xaxis.set_visible(False)
    #ax.yaxis.set_visible(False)
    #x = np.arange(len(names))
    rect=ax.bar(x-width/2, dft, width, color=cmaps[0], lw=1, edgecolor='k', label=lbl[0], hatch='+')
    rect=ax.bar(x+width/2, opt, width, color=cmaps[1], lw=1, edgecolor='k', label=lbl[1], hatch='//')
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.grid(axis='y', ls='--')
    #ax.set_yscale('log')
    #ax.set_xlim(0, np.sum(data, axis=1).max())
    #ax.set_ylim(-0.4, 7.4)


