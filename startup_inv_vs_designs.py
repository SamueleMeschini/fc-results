import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

data = np.genfromtxt("data/startup_inventory_vs_designs.csv", delimiter=',', names=True, usecols=range(1,3))
names = ['ARC', 'STEP EBB', 'STEP Li']
I_st_w_res = data['I_st_w_reskg']
I_st_wo_res = data['I_st_wo_reskg']
fig,ax = plt.subplots()
def subcategorybar(X, vals, width=0.6):
    n = len(vals)
    _X = np.arange(len(X))
    for i in range(n):
        if i == 1:
            rect1 = ax.bar(_X - width/2. + i/float(n)*width, vals[i], 
            width=width/float(n), align="edge", color='firebrick')  
        else:
            rect2 = ax.bar(_X - width/2. + i/float(n)*width, vals[i], 
            width=width/float(n), align="edge", color='forestgreen')  

    ax.bar_label(rect1, padding=3)
    ax.bar_label(rect2, padding=3)
    ax.set_ylim(0,10)
    ax.set_xticks(_X, X)
    ax.set_yticks([0,5,10])
    ax.set_ylabel("Start-up Inventory (kg)")
    ax.legend(["Startup w/o reserve","Startup with reserve"])
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

subcategorybar(names, [I_st_wo_res, I_st_w_res])
plt.tight_layout()
plt.savefig("startup_inv_vs_designs.pdf")
plt.show()
