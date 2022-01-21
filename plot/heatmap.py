import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

def draw_heatmap(ax, name, data):
    #im = ax.imshow(data, cmap='gray')
    #im = ax.imshow(data, cmap='gist_heat')
    im = ax.imshow(data, cmap='bone')
    ax.set_title(name,fontsize=10)
    ax.set_xticks(np.arange(0,20,5))
    ax.set_yticks(np.arange(8))
    #ax.set_xticklabels(sGPU)
