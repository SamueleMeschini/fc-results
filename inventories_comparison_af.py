import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotx
import matplotlib.cm as cm
from matplotlib.colors import Normalize, LogNorm

plt.rcParams["font.size"] = "14"
data = np.genfromtxt(f"data/inventory_af_50.csv", delimiter=",", names=True)
x1 = (data['time_s']/3600/24).T
y1 = np.array((data['TES_inventory_kg'], data['ISS_inventory_kg'], data['storage_inventory_kg'])).T
t_d_1 = x1[(y1[:,2]>2*y1[0,2])][0]
data = np.genfromtxt(f"data/inventory_af_100.csv", delimiter=",", names=True)
x2 = (data['time_s']/3600/24).T
y2 = np.array((data['TES_inventory_kg'], data['ISS_inventory_kg'], data['storage_inventory_kg'])).T
t_d_2 = x2[(y2[:,2]>2*y2[0,2])][0]


fig,ax = plt.subplots()
# dummy plots for legend. More elegant solution here https://stackoverflow.com/questions/51054529/manipulate-linestyle-in-matplotlib-legend 

# use the same colors for both axs
plt.gca().set_prop_cycle(None)
dummy2 = plt.scatter(x=0, y=0, marker='s', label='TES')
dummy3 = plt.scatter(x=0, y=0, marker='s', label='ISS')
dummy4 = plt.scatter(x=0, y=0, marker='s', label='Storage')
af1 = plt.plot(0, 1, c='k', linestyle='-', label='AF = 50%')
af2 = plt.plot(0, 1, c='k', linestyle='--', label='AF = 100%')
ax.loglog(x1[::10], y1[::10,:], linestyle='-')
plt.gca().set_prop_cycle(None)
ax.loglog(x2[::10], y2[::10,:], linestyle='--')
ax.vlines(t_d_1, ymin=0, ymax=1, colors='k', linestyles='-',transform=ax.get_xaxis_transform())
ax.vlines(t_d_2, ymin=0, ymax=1, colors='k', linestyles='--',transform=ax.get_xaxis_transform())
ax.set_xlim(1e-1,3*1e3)
ax.set_ylim(1e-3,1e2)
ax.set_xlabel('Time (days)')
ax.set_ylabel('Inventory (kg)')
ax.grid(True, which='both', alpha=0.1)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles, labels=labels, loc='upper left', ncol=2, fontsize=11)
ax.annotate('$t_d = 1y$', xy=(t_d_2, 2*y2[0,2]),  xycoords='data',
    xytext=(250, 40), textcoords='data', fontsize=12,
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3"),
    horizontalalignment='right', verticalalignment='top',
    )   
ax.annotate('$t_d = 2y$', xy=(t_d_1, 2*y1[0,2]),  xycoords='data',
    xytext=(3000, 40), textcoords='data', fontsize=12,
    arrowprops=dict(arrowstyle="->",
                    connectionstyle="arc3"),
    horizontalalignment='right', verticalalignment='top',
    )   
# ax.text(x=0.1*365, y=40, s='$t_d = 1y$')
# ax.text(x=2*365, y=50, s='$t_d = 2y$')

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
fig.savefig("inventories_af_comparison.pdf", dpi=300)