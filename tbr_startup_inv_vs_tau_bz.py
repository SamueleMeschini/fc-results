import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

TBE_values = [0.5, 1, 2, 5]  # %

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

for TBE in TBE_values:
    data = np.genfromtxt(
        f"data/t_blanket/TBE={TBE:.1f}%.csv", delimiter=",", names=True
    )
    plt.sca(axs[0])  # sca stands for Set Current Axis (activates the top axis)
    plt.plot(
        data["t_blanket_h"],
        data["TBR_req"],
        label="TBE = " + f"{TBE:.1f}%",
        marker=".",
    )
    plt.sca(axs[1])
    plt.plot(
        data["t_blanket_h"],
        data["I_startup_kg"],
        label="TBE = " + f"{TBE:.1f}%",
        marker=".",
    )

axs[1].set_xlabel(r"Blanket residence time $\tau_\mathrm{BZ}$ (h)")
axs[1].set_xscale("log")

for ax in axs:
    matplotx.line_labels(ax, fontsize=10)
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.grid(which="major", axis="y", alpha=0.1)

matplotx.ylabel_top("Required TBR", ax=axs[0])
matplotx.ylabel_top("Startup \n inventory (kg)", ax=axs[1])

axs[0].set_ylim(bottom=1)
axs[1].set_ylim(bottom=0)


plt.tight_layout()
plt.savefig("tbr_startup_inv_vs_tau_bz.pdf")
plt.show()
