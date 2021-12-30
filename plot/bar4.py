import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add


apps=[
"pr", 
"sssp",
]

names=[
"LJ",
"OR",
#"SW",
"TW",
#"CF",
"U2",
#"AR",
"IT",
#"U5",
#"WB",
"TX",
"CA",
"GM",
"USA",
"EU",
]

def draw_bar(ax, app):
    lbl = ["default", "optimal"]
    cmaps = ["k", "tan"]
    new_path="./new_%s.etl" % (app)
    old_path="./old_%s.etl" % (app)
    dft = np.loadtxt(old_path).T
    opt = np.loadtxt(new_path).T
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

fig, axs = plt.subplots(2, 1, sharex=True,sharey=False)
for i in range(2):
    draw_bar(axs[i], apps[i])

handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0.35), ncol=4)
#fig.legend(handles, labels, loc='lower center', ncol=4)
plt.tight_layout()
fig.subplots_adjust(bottom=0.5)
plt.show()

