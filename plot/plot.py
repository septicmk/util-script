import matplotlib.pyplot as plt
import numpy as np
import sys, os

# TODO (mengke): implement a reusable plot lib in your spare time.
# A art is a actor, describe the profile of the colormap, markers and styles, It can 
# - generate a layout
# - provide APIs to visualize data in a single call
class Art:
    def __init__(self):
        pass

    def composition(self, x, y):
        pass

    def add_meta(self, ax, xlabel=None, ylabel=None, grid=False, xlog=False, ylog=False, xrevert=False, legend=0):
        if xlabel!=None: ax.set_xlabel(xlabel)
        if ylabel!=None: ax.set_ylabel(ylabel)
        if grid:
            ax.grid(ls='--')
            ax.set_axisbelow(True)
        if xlog: ax.set_xscale('log')
        if ylog: ax.set_yscale('log')
        #ax.legend(frameon=False, prop={'size': 6})
        ax.legend(prop={'size': 6})

    # The key feature.
    # generates a layout that fit the given width, with suitable fontsize and avoids the overlapping of legend/labels
    def gen_layout(self):
        pass

    # --------------------------------------------------------------------------
    ##
    # @Synopsis draw on stack, if len(data[i][j]) = 1, then this is a 
    #
    # @Param ax: the axis 
    # @Param data: 2-D data[i][j], stack data[i+1] on data[i]
    # @Param cmap: colormap, hatchmap
    #
    # @Returns  None
    # --------------------------------------------------------------------------
    def __bar_one_stack(self, ax, x, data, w, cmap=None, hmap=None):
        ax.bar(x, data[0], w, color=cmap, lw=1, edgecolor='k',)

    def bar(self, ax, data, cmap):
        pass

    def barh(self, ax, data, cmap):
        pass

    def line(self, ax, data, cmap):
        pass

    def heat(self, ax, data, cmap):
        pass
