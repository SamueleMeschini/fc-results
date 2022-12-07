import numpy as np
import matplotlib.pyplot as plt
import matplotx


eta_f_f_b_values = [0.5, 1, 2, 5]  # %

# create a new figure
fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(6.4, 6))

# iterate through etaf fb values
for eta_f_f_b in eta_f_f_b_values:
    data = np.genfromtxt(
        f"data/t_res/eta_f x f_b = {eta_f_f_b:.1f}%.csv", delimiter=",", names=True
    )
    plt.sca(axs[0])
    # fetch csv data with numpy
    plt.plot(data["t_res"], data["TBR"], label=f"TBE = {eta_f_f_b:.1f}%")
    plt.sca(axs[1])
    plt.plot(data["t_res"], data["I_startup_kg"], label=f"TBE = {eta_f_f_b:.1f}%")

plt.xlabel("Reserve time $t_\mathrm{res}$ (h)")

# Linear yscale should always start at zero
axs[0].set_ylim(bottom=1)
axs[1].set_ylim(bottom=0)
axs[0].set_ylabel("Required TBR")
axs[1].set_ylabel("Startup inventory (kg)")


# remove top and right axis, cause we don't need that junk
for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.set_xlim(left=0)
    # Use inline labelling
    matplotx.line_labels(ax)
plt.tight_layout()

# save and show
plt.savefig("tbr_startup_inv_vs_reserve_time.pdf")
plt.show()
