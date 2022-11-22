import numpy as np
import matplotlib.pyplot as plt
import matplotx


eta_f_f_b_values = [0.5, 1, 2, 5]  # %

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

for eta_f_fb in eta_f_f_b_values:
    data = np.genfromtxt(
        f"data/t_blanket/eta_f x f_b = {eta_f_fb:.1f}%.csv", delimiter=",", names=True
    )
    plt.sca(axs[0])  # sca stands for Set Current Axis (activates the top axis)
    plt.plot(
        data["t_blanket_h"], data["TBR"], label="$\eta_f \ f_b =$" + f"{eta_f_fb:.1f}%"
    )
    plt.sca(axs[1])
    plt.plot(
        data["t_blanket_h"],
        data["I_startup_kg"],
        label="$\eta_f \ f_b =$" + f"{eta_f_fb:.1f}%",
    )

axs[1].set_xlabel(r"Blanket residency time $\tau_\mathrm{BZ}$ (h)")
axs[1].set_xscale("log")

for ax in axs:
    matplotx.line_labels(ax)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)

matplotx.ylabel_top("Required TBR", ax=axs[0])
matplotx.ylabel_top("Startup \n inventory (kg)", ax=axs[1])

axs[0].set_ylim(bottom=1)
axs[1].set_ylim(bottom=0)


plt.tight_layout()
plt.savefig("tbr_startup_inv_vs_tau_bz.pdf")
plt.show()
