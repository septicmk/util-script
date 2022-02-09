import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

#labels = ["Arrow Read", "Arrow Write", "Java Read", "Java Write", "FFI Read", "FFI Write", "ONI Read", "ONI Write"]
#xname = ["1M", "2M", "4M", "8M", "16M", "32M"]
#colors = ['k', 'b', 'r', 'g']
#markers = ['^', 'v', 'o', 's']
def draw_lines(ax, xname, data, labels, colors, markers):
    x = np.array(range(len(xname)))
        
    ax.plot(x, data[0], label = labels[0], color = colors[0], marker = markers[0], linestyle = '--')
    ax.plot(x, data[1], label = labels[1], color = colors[0], marker = markers[0])

    ax.plot(x, data[2], label = labels[2], color = colors[1], marker = markers[1], linestyle = '--')
    ax.plot(x, data[3], label = labels[3], color = colors[1], marker = markers[1])

    ax.plot(x, data[4], label = labels[4], color = colors[2], marker = markers[2], linestyle = '--')
    ax.plot(x, data[5], label = labels[5], color = colors[2], marker = markers[2])

    ax.plot(x, data[6], label = labels[6], color = colors[3], marker = markers[3], linestyle = '--')
    ax.plot(x, data[7], label = labels[7], color = colors[3], marker = markers[3])

    ax.set_ylabel("Latency (us/op)")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.legend(frameon=False, prop={'size': 6})
    ax.legend(prop={'size': 6})

def draw_lines(ax, xname, data, labels, colors, markers):
    x = np.array(range(len(xname)))
       
    ax.plot(x, data[0], label = labels[0], color = colors[0], marker = markers[0])
    ax.plot(x, data[1], label = labels[1], color = colors[0], marker = markers[1])
    ax.plot(x, data[2], label = labels[2], color = colors[1], marker = markers[2])
    ax.plot(x, data[3], label = labels[3], color = colors[1], marker = markers[3])
    ax.set_ylabel("Time (s)")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.legend(frameon=False, prop={'size': 6})
    #ax.set_ylim(0, 100)
    ax.legend(prop={'size': 10}, ncol=2)

#labels = ["DF Incbuild", "DF ReBuild", "Graph Incbuild", "Graph ReBuild"]
#colors = [ycmap[0], ycmap[1]]
#markers = ['^', 'o', 'v', 's']
def draw_lines2(ax, xname, data, labels, colors, markers):
    x = np.array(range(len(xname)))
       
    ax.plot(x, data[0], label = labels[0], color = colors[0], marker = markers[0], linestyle = '--')
    ax.plot(x, data[1], label = labels[1], color = colors[0], marker = markers[1], linestyle = '--')
    ax.plot(x, data[2], label = labels[2], color = colors[1], marker = markers[2], linestyle = '--')
    ax.plot(x, data[3], label = labels[3], color = colors[1], marker = markers[3], linestyle = '--')
    ax.set_ylabel("Memory Footprint (GB)")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.set_ylim(0, 5000)
    #ax.legend(frameon=False, prop={'size': 6})
    ax.legend(prop={'size': 10}, ncol=2)
