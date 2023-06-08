import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

TBE_values = [0.5, 1, 2, 5]  # %

# create a new figure
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

# iterate through etaf fb values
for TBE in TBE_values:
    data = np.genfromtxt(
        f"data/t_res/TBE={TBE:.1f}%.csv", delimiter=",", names=True
    )
    plt.sca(axs[0])
    # fetch csv data with numpy
    plt.plot(data["t_res"], data["TBR_req"], label=f"TBE = {TBE:.1f}%", marker='.')
    plt.sca(axs[1])
    plt.plot(data["t_res"], data["I_startup_kg"], label=f"TBE = {TBE:.1f}%", marker='.')

plt.xlabel("Reserve time $t_\mathrm{res}$ (h)")

# Linear yscale should always start at zero
axs[0].set_ylim(bottom=1)
axs[0].set_xticks([0,24,48])
axs[0].set_yticks(np.arange(1., 1.5, 0.1))

axs[1].set_ylim(bottom=0)
axs[1].set_yticks(np.arange(0, 12, 2))


matplotx.ylabel_top("Required TBR", ax=axs[0])
matplotx.ylabel_top("Startup \n inventory (kg)", ax=axs[1])


# remove top and right axis, cause we don't need that junk
for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.set_xlim(left=0)
    # Use inline labelling
    matplotx.line_labels(ax)
    ax.grid(which="major", axis="y", alpha=0.1)

plt.tight_layout()

# save and show
plt.savefig("tbr_startup_inv_vs_reserve_time.eps", format='eps')
plt.show()
