import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

def draw_runtime(ax, name, b, l):
    data = [[],[],[],[],[],[],[],[]]
    path="../pr_time_avg/pr_%s.etl" % (name)
    d = np.loadtxt(path).T
    for i in range(len(d)):
        if i < b*8 : continue
        if i >=(b+l)*8: continue
        h = i%8
        data[h].append(d[i]);
    sz = len(data[0])
    #data = [[data[i][j] for i in range(8)] for j in range(sz)]

    #p = sum(sum(data))
    #im = ax.imshow(data, cmap='gray')
    #im = ax.imshow(data, cmap='gist_heat')
    im = ax.imshow(data, cmap='bone')
    ax.set_title(name,fontsize=10)
    ax.set_xticks(np.arange(0,20,5))
    ax.set_yticks(np.arange(8))
    ## ... and label them with the respective list entries
    #ax.set_xticklabels(sGPU)


