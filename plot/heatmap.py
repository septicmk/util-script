import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

def draw_heatmap(ax, data, cmaps, name):
    im = ax.imshow(data, cmap=cmaps) # gray gist_heat
    ax.set_title(name, fontsize=10)
    #ax.set_xticks(np.arange(0,20,5))
    #ax.set_yticks(np.arange(8))
    #ax.set_xticklabels(sGPU)
