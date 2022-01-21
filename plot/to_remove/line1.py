import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

def draw_lines(ax):
    names = ["./1M.txt", "./2M.txt", "./4M.txt", "./8M.txt", "./16M.txt", "./32M.txt"]
    x = ["1M", "2M", "4M", "8M", "16M", "32M"]
    labels = ["Arrow Read", "Arrow Write", "Java Read", "Java Write", "FFI Read", "FFI Write", "ONI Read", "ONI Write"]
    colors = ['k', 'b', 'r', 'g']
    markers = ['^', 'v', 'o', 's']
    arrow_read = []
    arrow_write = []
    FFI_read = []
    FFI_write = []
    Java_read = []
    Java_write = []
    ONI_read = []
    ONI_write = []
    for name in names:
        _d = np.array(np.loadtxt(name)).T
        arrow_read.append(_d[0])
        arrow_write.append(_d[1])
        FFI_read.append(_d[2])
        FFI_write.append(_d[3])
        Java_read.append(_d[4])
        Java_write.append(_d[5])
        ONI_read.append(_d[6])
        ONI_write.append(_d[7])
        
    ax.plot(x, arrow_read, label = labels[0], color = colors[0], marker = markers[0], linestyle = '--')
    ax.plot(x, arrow_write, label = labels[1], color = colors[0], marker = markers[0])
    ax.plot(x, Java_read, label = labels[2], color = colors[1], marker = markers[1], linestyle = '--')
    ax.plot(x, Java_write, label = labels[3], color = colors[1], marker = markers[1])
    ax.plot(x, FFI_read, label = labels[4], color = colors[2], marker = markers[2], linestyle = '--')
    ax.plot(x, FFI_write, label = labels[5], color = colors[2], marker = markers[2])
    ax.plot(x, ONI_read, label = labels[6], color = colors[3], marker = markers[3], linestyle = '--')
    ax.plot(x, ONI_write, label = labels[7], color = colors[3], marker = markers[3])
    ax.set_ylabel("Latency (us/op")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.legend(frameon=False, prop={'size': 6})
    ax.legend(prop={'size': 6})

#plt.figure()
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
    cmaps = ["k", "tan"]
    lbl = ["Store", "Load"]
    x = np.array([0, 1])
    xname = ["filesystem", "plasma"]
    ax.bar(x-width/2, base[0], width, color=cmaps[0], lw=1, edgecolor='k', label = lbl[0], hatch = '+')
    ax.bar(x+width/2, plasma[0], width, color=cmaps[0], lw=1, edgecolor='k', hatch = '+')

    ax.bar(x-width/2, base[1], width, bottom=base[0], color=cmaps[1], lw=1, edgecolor='k', label = lbl[1], hatch = '//')
    ax.bar(x+width/2, plasma[1], width, bottom=plasma[0], color=cmaps[1], lw=1, edgecolor='k', hatch = '//')

    _ax.bar(x-width/2, over, width, color=cmaps[1], lw=1, edgecolor='k', label = lbl[0], hatch = '//')
    _ax.bar(x+width/2, [0,0], width, color=cmaps[0],lw=1, edgecolor='k', label=lbl[1], hatch='+')
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

def draw_bar(ax):
    data = np.array(np.loadtxt("1M.txt"))
    arrow = data[0:2]
    FFI   = data[2:4]
    Java  = data[4:6]
    w = 0.25;
    x = np.array([0, 1])
    xname = ["Read", "Write"]
    ax.bar(x-w, arrow, w, label ="Arrow", lw=1, edgecolor='k', color='k')
    ax.bar(x, Java, w, label ="Java", edgecolor='k', color=ycmap[3])
    ax.bar(x+w, FFI, w, label ="FFI", edgecolor='k', color=ycmap[1])
    ax.set_yscale('log')
    ax.set_ylabel('Latency (us/op)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    ax.legend(prop={'size': 12})

#fig = plt.figure(constrained_layout=False)
#gs = fig.add_gridspec(2, 3)
#
#ax2 = fig.add_subplot(gs[1,0])
#ax1 = fig.add_subplot(gs[0,0], sharex = ax2)
#
#ax3 = fig.add_subplot(gs[:,1])
#ax4 = fig.add_subplot(gs[:,2])
#
#draw_stack_bar(ax1, ax2);
#draw_lines(ax3)
#draw_bar(ax4)

fig, axs = plt.subplots(1, 1, sharex=True,sharey=False)
for i in range(1):
    draw_bar(axs)


handles, labels = axs.get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
fig.legend(handles, labels, loc='lower center', ncol=3)
plt.tight_layout()
fig.subplots_adjust(bottom=0.12)
plt.show()

