import numpy as np
import matplotlib
import matplotlib.pyplot as plt

t_bz_values = [1]

matplotlib.style.use('seaborn-v0_8-deep')

for t_bz in t_bz_values:    
    data = np.genfromtxt(f"data/inventory_evolution_tbz{t_bz}d.csv", delimiter=",", names=True)
    x = (data['t']/3600/24).T
    y = np.array((data['I_bz'], data['I_tes'], data['I_iss'], data['I_storage'])).T

    fig,ax = plt.subplots()

    ax.loglog(x, y)
    ax.vlines(2*365, ymin=0, ymax=1, colors='k', linestyles='--',transform=ax.get_xaxis_transform())
    ax.set_xlim(1e-1,1e3)
    ax.set_ylim(1e-3,1e2)
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Inventory (kg)')
    ax.grid(True, which='both', alpha=0.1)
    ax.legend(['Breeding zone', 'TES', 'ISS', 'Storage'], loc='upper left')
    ax.text(x=0.7*365, y=50, s='$t_d = 2y$')
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    plt.show()
    fig.savefig(f'inventories_vs_t_tbz{t_bz}d.eps', format='eps', dpi=300)