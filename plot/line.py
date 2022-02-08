import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

def draw_lines(ax, xname, data, labels, colors, markers):
    #names = ["./1M.txt", "./2M.txt", "./4M.txt", "./8M.txt", "./16M.txt", "./32M.txt"]
    #x = ["1M", "2M", "4M", "8M", "16M", "32M"]
    x = np.array(range(len(xname)))
    #labels = ["Arrow Read", "Arrow Write", "Java Read", "Java Write", "FFI Read", "FFI Write", "ONI Read", "ONI Write"]
    #colors = ['k', 'b', 'r', 'g']
    #markers = ['^', 'v', 'o', 's']
        
    ax.plot(x, arrow_read, label = labels[0], color = colors[0], marker = markers[0], linestyle = '--')
    ax.plot(x, arrow_write,label = labels[1], color = colors[0], marker = markers[0])
    ax.plot(x, Java_read,  label = labels[2], color = colors[1], marker = markers[1], linestyle = '--')
    ax.plot(x, Java_write, label = labels[3], color = colors[1], marker = markers[1])
    ax.plot(x, FFI_read,   label = labels[4], color = colors[2], marker = markers[2], linestyle = '--')
    ax.plot(x, FFI_write,  label = labels[5], color = colors[2], marker = markers[2])
    ax.plot(x, ONI_read,   label = labels[6], color = colors[3], marker = markers[3], linestyle = '--')
    ax.plot(x, ONI_write,  label = labels[7], color = colors[3], marker = markers[3])
    ax.set_ylabel("Latency (us/op)")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.legend(frameon=False, prop={'size': 6})
    ax.legend(prop={'size': 6})

def draw_lines(ax, xname, data, labels, colors, markers):
    x = np.array(range(len(xname)))
       
    ax.plot(x, df_inc_build_time, label = labels[0], color = colors[0], marker = markers[0])
    ax.plot(x, df_re_build_time,  label = labels[1], color = colors[0], marker = markers[1])
    ax.plot(x, g_inc_build_time,  label = labels[2], color = colors[1], marker = markers[2])
    ax.plot(x, g_re_build_time,   label = labels[3], color = colors[1], marker = markers[3])
    ax.set_ylabel("Time (s)")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.legend(frameon=False, prop={'size': 6})
    #ax.set_ylim(0, 100)
    ax.legend(prop={'size': 10}, ncol=2)

def draw_lines2(ax, xname, data, labels, colors, markers):
    x = np.array(range(len(xname)))
    #labels = ["DF Incbuild", "DF ReBuild", "Graph Incbuild", "Graph ReBuild"]
    #colors = [ycmap[0], ycmap[1]]
    #markers = ['^', 'o', 'v', 's']
       
    ax.plot(x, df_inc_build_mem, label = labels[0], color = colors[0], marker = markers[0], linestyle = '--')
    ax.plot(x, df_re_build_mem,  label = labels[1], color = colors[0], marker = markers[1], linestyle = '--')
    ax.plot(x, g_inc_build_mem,  label = labels[2], color = colors[1], marker = markers[2], linestyle = '--')
    ax.plot(x, g_re_build_mem,   label = labels[3], color = colors[1], marker = markers[3], linestyle = '--')
    ax.set_ylabel("Memory Footprint (GB)")
    ax.set_xlabel("Object size (GB)")
    ax.set_yscale('log')
    ax.grid(ls='--')
    ax.set_axisbelow(True)
    #ax.set_ylim(0, 5000)
    #ax.legend(frameon=False, prop={'size': 6})
    ax.legend(prop={'size': 10}, ncol=2)
