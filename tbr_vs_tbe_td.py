import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(6.4, 6))

for td in [1, 2, 5]:
    data = np.genfromtxt(
        f"data/td/t_d ={td}y.csv", delimiter=",", names=True
    )

    TBE = data["TBE"]*100

    plt.sca(axs[0])
    plt.plot(TBE, data["TBR_req"], label=f"$t_d = {td}$ y", marker='.')
    plt.sca(axs[1])
    plt.plot(TBE, data["TBR_req"], label=f"$t_d = {td}$ y", marker='.')


plt.xlabel("TBE (%)")

# set limits
# plt.xlim(right=10.2)
axs[1].set_ylim(1,1.3)

matplotx.ylabel_top("Required TBR", ax=axs[0])
matplotx.ylabel_top("Required TBR", ax=axs[1])


# remove top and right axis, cause we don't need that junk
for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    # Use inline labelling
    matplotx.line_labels(ax)
    ax.grid(which="major", axis="y", alpha=0.1)

plt.tight_layout()

plt.savefig("tbr_vs_tbe_td.eps", format='eps')

plt.show()
