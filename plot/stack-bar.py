import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]
#plt.figure()
def draw_stack_bar(ax):
    lbl = ["comp", "overhead"]
    comp     =   np.array([53, 53, 53])
    overhead = np.array([0, 23, 50.4])
    cmaps = [ycmap[1], ycmap[0]]
    x = np.array([0.2, 1, 1.8])
    xname = ["co-location", "replication", "evivtion"]
    width = 0.35
    ax.bar(x, comp, width, color=cmaps[0], lw=1, edgecolor='k', label = lbl[0])
    ax.bar(x, overhead, width, bottom=comp, color=cmaps[1], lw=1, edgecolor='k', label = lbl[1])

    #_ax.get_xaxis().set_visible(False)
    ax.set_ylabel('Runtime (s)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    ax.set_ylim(0,110)
    ax.legend(prop={'size': 10})
    # ax.set_yscale('log')


fig, axs = plt.subplots(1, 1, sharex=False, sharey=True)
draw_stack_bar(axs)


handles, labels = axs.get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
fig.legend(handles, labels, loc='lower center', ncol=2)
plt.tight_layout()
fig.subplots_adjust(bottom=0.12)
plt.show()


