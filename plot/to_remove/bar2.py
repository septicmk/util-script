#!/usr/bin/env python3
import matplotlib.pyplot as plt
from numpy.core.defchararray import array
from scipy.interpolate import make_interp_spline
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

def draw_smooth_curve(ax):
    data = np.loadtxt("./data-p.log")
    mem = []
    cpu = []
    for i in range(len(data)):
        if i&1: cpu.append(data[i])
        else : mem.append(data[i])

    x = np.array(range(len(data)//2))
    mem = np.array(mem)
    cpu = np.array(cpu)
    spline_mem = make_interp_spline(x, mem)
    spline_cpu = make_interp_spline(x, cpu)

    ax.grid(ls='--')
    ax.set_axisbelow(True)
    
    x = np.linspace(x.min(), x.max(), 500)
    mem = spline_mem(x) 
    cpu = spline_cpu(x)
    ax.plot(x, mem, color = ycmap[0], label="Memory")
    ax.plot(x, cpu, color = ycmap[1], label ="CPU")

def draw_bar(ax):
    data = np.array([
        [2439.45, 164.634765],
        [50.5063, 52.421669],
        [56.4439, 14.584431]
        ])
    w = 0.25;
    x = np.array([0, 1])
    xname = ["Grape", "DGL"]
    ax.bar(x-w, data[0], w, label="IO", lw=1, edgecolor='k', color='k', hatch='+')
    ax.bar(x, data[1], w, label="Serialization", edgecolor='k', color='dimgray', hatch='/')
    ax.bar(x+w, data[2], w, label ="Deserialization", edgecolor='k', color='white', hatch='\\')
    ax.set_yscale('log')
    ax.set_ylabel('Runtime (s)')
    ax.set_xticks(x)
    ax.set_xticklabels(xname)
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    ax.legend(prop={'size': 6})

fig = plt.figure(constrained_layout=False)
gs = fig.add_gridspec(1, 2)

ax1 = fig.add_subplot(gs[0,:2])
#ax2 = fig.add_subplot(gs[0,2])

draw_smooth_curve(ax1)

#ax2.xaxis.grid(ls='--')


handles, labels = ax1.get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
fig.legend(handles, labels, loc='lower center', ncol=4)
plt.tight_layout()
#fig.subplots_adjust(bottom=0.12)
plt.show()

