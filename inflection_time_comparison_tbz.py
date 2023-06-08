import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotx
import matplotlib.cm as cm
from matplotlib.colors import Normalize, LogNorm

matplotlib.style.use('seaborn-v0_8-deep')
plt.rcParams["font.size"] = "14.5"
t_bz_values = [1, 240]

for t_bz in t_bz_values:    
    data = np.genfromtxt(f"data/inventory_evolution_tbz{t_bz}h.csv", delimiter=",", names=True)
    x = (data['time_s']/3600/24).T
    y = np.array((data['blanket_inventory_kg'], data['TES_inventory_kg'], data['ISS_inventory_kg'], data['storage_inventory_kg'])).T
    t_infl = x[np.argmin(data['storage_inventory_kg'])]
    fig,ax = plt.subplots()

    ax.loglog(x, y)
    ax.vlines(2*365, ymin=0, ymax=1, colors='k', linestyles='--',transform=ax.get_xaxis_transform())
    ax.annotate('Inflection point', xy=(t_infl, np.min(data['storage_inventory_kg'])),  xycoords='data',
            xytext=(250, 180), textcoords='axes points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            horizontalalignment='right', verticalalignment='top',
            )   
    ax.set_xlim(1e-1,1e3)
    ax.set_ylim(1e-3,1e2)
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Inventory (kg)')
    ax.grid(True, which='both', alpha=0.1)
    ax.legend(['Breeding zone', 'TES', 'ISS', 'Storage'], loc='upper left', fontsize=11)
    ax.text(x=0.4*365, y=50, s='$t_d = 2y$')
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    plt.tight_layout()
    fig.savefig(f'inventories_vs_t_tbz{t_bz}h.eps', format='eps', dpi=300)