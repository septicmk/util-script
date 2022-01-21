import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

def draw_barh0(ax):
    lbl = ["ORD+ORD", "ORD+ORDf", "ORDf+ORD", "ORDf+ORDf", "Alluxio"]
    itg  = [345, 215, 130, 0, 0]
    cmaps = ["k", "dimgray", "gray", "lightgray", "w", "r"]
    rect=ax.barh(lbl, itg, 0.6, color=cmaps, lw=1, edgecolor='k', label=lbl)
    ax.invert_xaxis()
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(True)
    #ax.set_xscale('log')

def draw_barh1(ax):
    lbl = ["ORD+ORD", "ORD+ORDf", "ORDf+ORD", "ORDf+ORDf", "Alluxio"]
    perf = [71.3,  95.6, 110.9, 135.2, 238.4]
    cmaps = ["k", "dimgray", "gray", "lightgray", "r"]
    #ax.invert_yaxis()
    #ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(True)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #data = list(map(lambda x: x/data[0], perf))
    #data = list(map(lambda x: 1/x, data))
    rect=ax.barh(lbl, perf, 0.6, color=cmaps, lw=1, edgecolor='k', label=lbl)
    #ax.set_xlim(-0.5, 5.5)
    #ax.set_ylim(0, 1)

fig, axs = plt.subplots(1, 2, sharex=False, sharey=True)
draw_barh0(axs[0])
draw_barh1(axs[1])


handles, labels = axs[0].get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
fig.legend(handles, labels, loc='lower center', ncol=5)
plt.tight_layout()
fig.subplots_adjust(bottom=0.12)
plt.show()


