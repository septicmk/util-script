import numpy as np
import matplotlib
import matplotlib.pyplot as plt

sGPU = ["GPU0", "GPU1", "GPU2", "GPU3", "GPU4", "GPU5", "GPU6", "GPU7"]
dGPU = ["GPU0", "GPU1", "GPU2", "GPU3", "GPU4", "GPU5", "GPU6", "GPU7"]


data = np.loadtxt("./uk-2002-hash")
#data = np.loadtxt("./europe_osm-hash")
p = sum(sum(data))
data = data/p
t = 0
print(data)
for i in range(8): t = t + data[i][i]
print(t, 1-t)

fig, ax = plt.subplots()
im = ax.imshow(data, cmap='hot', norm=None)

# We want to show all ticks...
ax.set_xticks(np.arange(len(sGPU)))
ax.set_yticks(np.arange(len(dGPU)))

# ... and label them with the respective list entries
ax.set_xticklabels(sGPU)
ax.set_yticklabels(dGPU)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
#for i in range(len(sGPU)):
#    for j in range(len(dGPU)):
#        text = ax.text(j, i, data[i, j],
#                       ha="center", va="center", color="w")

ax.set_title("edges between two GPUs")
fig.tight_layout()
plt.show()

