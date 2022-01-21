import matplotlib.pyplot as plt
import numpy as np
import sys
from operator import add

ycmap = ["#F7bc15", "#1a3ac5", "#3366ff", "#Abcbf6"]
#plt.figure()
fig, axs = plt.subplots(1, 1, sharex=False, sharey=True)
draw_stack_bar(axs)


handles, labels = axs.get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=4)
#fig.legend(handles, labels, loc='lower center', ncol=2)
plt.tight_layout()
fig.subplots_adjust(bottom=0.12)
plt.show()


