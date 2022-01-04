import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import math

def save_graph(graph,file_name, values, nsz):
    #initialze Figure
    plt.figure(num=None, figsize=(20, 20), dpi=80)
    plt.axis('off')
    fig = plt.figure(1)
    #pos = nx.spring_layout(graph)
    #nx.draw_networkx_nodes(graph,pos)
    #nx.draw_networkx_edges(graph,pos)
    #nx.draw_networkx_labels(graph,pos)

    nx.draw(graph, pos=pos, cmap=plt.get_cmap('hsv'), node_color=values, node_size=nsz, width=0.05)
    # bwr

    #cut = 1.00
    #xmax = cut * max(xx for xx, yy in pos.values())
    #ymax = cut * max(yy for xx, yy in pos.values())
    #plt.xlim(0, xmax)
    #plt.ylim(0, ymax)

    plt.savefig(file_name, bbox_inches="tight")
    plt.close()
    del fig

#Assuming that the graph g has nodes and edges entered
#G = nx.Graph()
G = nx.read_edgelist('soc-bitcoin-rinse.ev')
V = np.loadtxt("hist.log");
nv, ne = G.number_of_nodes(), G.number_of_edges()
ideg = {}
odeg = {}
mideg=0
modeg=0
for i in G.nodes():
    v = int(i)
    ideg[v] = V[v][0]
    odeg[v] = V[v][1]
    mideg = max(mideg, ideg[v])
    modeg = max(modeg, odeg[v])

def lgdeg(base, val):
    if val == 0: return 0
    return math.log(float(val)/float(base))
pos = nx.spring_layout(G, k=0.15, iterations=10, seed=2)
#pos = nx.circular_layout(G)
#pos = nx.spiral_layout(G)
print (nv, ne)

def process(d):
    val_map = {}
    for i in G.nodes():
        v = int(i)
        val_map[v] = V[v][d+3]
    
    values = [0.5 + 0.5*val_map.get(int(node), 0) * lgdeg(modeg, odeg.get(int(node),0)) for node in G.nodes()]
    nsz = [val_map.get(int(node), 0)*50 for node in G.nodes()]
    
    #pos = nx.spring_layout(G, k=0.15, iterations=20)
    #nx.draw(G, pos=pos, cmap=plt.get_cmap('brg'), node_color=values, node_size=1, width=0.05)
    out='./png/'+str(d) +'.png'
    print("procssing..", out)
    save_graph(G, out, values, nsz)
    #plt.savefig(out)

if __name__ == '__main__':
    items = [ x for x in range(93) ]
    pool = mp.Pool(32)
    pool.map(process, items)
    pool.close()
    pool.join()


