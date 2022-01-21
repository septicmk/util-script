import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys

#names=[
##"livejournal_86M",
##"hollywood_113M",
##"orkut_213M",
##"sinaweibo_523M",
##"twitter_530M",
##"indochina_302M",
#"uk-2002_524M",
#"arabic_1.11B",
#"uk-2005_1.57B",
#"webbase_1.71B"
#]

names=[
"uk-2002",
"arabic-2005",
"uk-2005",
"webbase-2001"
]


def draw_edges(ax, name, b, l):
    path="../edges/sssp_%s_gpu_8.etl" % (name)
    d = np.loadtxt(path)
    x = range(l)
    for i in range(8):
        y = d[i][b:b+l]
        ax.plot(x,y,lw=2) 
        ax.set_yscale('log')

def draw_time(ax, name, b, l):
    path="../pr_time/sssp_%s_gpu_8.etl" % (name)
    d = np.loadtxt(path)
    for i in range(len(d)):
        if i < b*8 : continue
        if i >=(b+l)*8: continue
        h = i%8
        data[h].append(d[i]);
    x = range(l)
    for i in range(8):
        y = data[i]
        ax.plot(x,y,lw=2) 
        ax.set_yscale('log')

def draw_bar(ax, name, b, l):
    data = [[],[],[],[],[],[],[],[]]
    path="../time/sssp_%s_gpu_8.etl" % (name)
    d = np.loadtxt(path).T
    for i in range(len(d)):
        if i < b*8 : continue
        if i >=(b+l)*8: continue
        h = i%8
        data[h].append(d[i]);
    sz = len(data[0])
    data = [[data[i][j] for i in range(8)] for j in range(sz)]
    data = np.array(data)
    dsum = data.sum(axis=1)
    print (dsum.shape, data.shape)
    for i in range(sz):
        for j in range(8):
            data[i][j] = data[i][j] / dsum[i]
    data_cum = data.cumsum(axis=1)
    lbl = range(sz)
    cmaps = plt.get_cmap('gray')(np.linspace(0.15, 0.85, 8))
    for i in range(8):
        height = data[:, i]
        bottom = data_cum[:,i] - height
        ax.bar(lbl, height, 1, bottom=bottom, color=cmaps[i])
        ax.set_ylim(0, 1)
    

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

fig, axs = plt.subplots(4, 2, sharex=False, sharey=True)
for i in range(4):
    draw_runtime(axs[i][0], names[i], 0, 20)
    #draw_time(axs[i][1], names[0], 0, 20)

#fig, axs = plt.subplots(2, 5, sharex=False,sharey=False)
#for i in range(10):
#    draw_runtime(axs[i//5][i%5], names[i], 0, 20)

#handles, labels = axs[1][4].get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
#fig.legend(handles, labels, loc='lower center', ncol=4)

plt.tight_layout()
#fig.subplots_adjust(bottom=0.12)
plt.show()

