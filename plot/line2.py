import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]

df_inc_build_time = np.array([0.045, 0.104, 0.142, 0.164])
df_re_build_time  = np.array([0.33 , 0.66 , 0.96 , 1.38])
df_mem_base       = np.array([3.5,   7.0  , 10.55, 14.06])
df_re_build_mem        = np.array([4.22,  8.44 , 12.663, 16.88])
df_inc_build_mem       = df_re_build_mem - df_mem_base

g_inc_build_time = np.array([0.15, 0.31, 0.5, 0.57])
g_re_build_time  = np.array([4.92, 5.54, 10.8, 19.5])
g_mem_base       = np.array([218, 310, 493, 595])
g_re_build_mem        = np.array([219, 313, 496, 599])
g_inc_build_mem     = df_re_build_mem - df_mem_base

# group one
# df_inc_build_time
# df_re_build_time
# g_inc_build_time
# g_re_build_time

# group two
# df_inc_build_mem
# df_re_build_mem
# g_inc_build_mem
# g_re_build_mem

def draw_lines(ax):
    x = ["1", "2", "3", "4"]
    labels = ["DF Incbuild", "DF ReBuild", "Graph Incbuild", "Graph ReBuild"]
    colors = [ycmap[0], ycmap[1]]
    markers = ['^', 'o', 'v', 's']
       
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

def draw_lines2(ax):
    x = ["1", "2", "3", "4"]
    labels = ["DF Incbuild", "DF ReBuild", "Graph Incbuild", "Graph ReBuild"]
    colors = [ycmap[0], ycmap[1]]
    markers = ['^', 'o', 'v', 's']
       
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



fig, axs = plt.subplots(1, 2, sharex=True,sharey=False)
draw_lines(axs[0])
draw_lines2(axs[1])


#handles, labels = axs.get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
#fig.legend(handles, labels, loc='lower center', ncol=3)
plt.tight_layout()
#fig.subplots_adjust(bottom=0.12)
plt.show()

