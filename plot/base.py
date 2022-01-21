import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

fig = plt.figure(constrained_layout=False)
gs = fig.add_gridspec(2, 3)

ax2 = fig.add_subplot(gs[1,0])
ax1 = fig.add_subplot(gs[0,0], sharex = ax2)

ax3 = fig.add_subplot(gs[:,1])
ax4 = fig.add_subplot(gs[:,2])


#handles, labels = axs[0].get_legend_handles_labels()
#fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
fig.legend(handles, labels, loc='lower center', ncol=4)
plt.tight_layout()
#fig.subplots_adjust(bottom=0.12)
plt.show()

