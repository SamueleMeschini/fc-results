import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

TBE_values = [0.5, 1, 2, 5]  # %

fig, axs = plt.subplots(nrows=1, ncols=1, sharex=True)

for TBE in TBE_values:
    data = np.genfromtxt(
        f"data/AF/TBE={TBE:.1f}%.csv", delimiter=",", names=True
    )
    plt.plot(
        data["AF"],
        data["TBR_req"],
        label="TBE = " + f"{TBE:.1f}%",
        marker=".",
    )
plt.vlines([94,97], [1.,1.], [1.38,1.38], colors='k', linestyles='--')
axs.set_xlabel(r"Availability Factor (%)")

matplotx.line_labels(axs, fontsize=10)
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
axs.set_ylabel("Required TBR")
axs.grid(which="major", axis="y", alpha=0.1)
axs.set_ylim(1,1.4)
plt.text(77,1.35,'$t_{pulse}$ = 1800s \n $t_{off}$ = 120s', bbox=dict(facecolor='white', edgecolor='k'), fontsize=12)
plt.text(99,1.3,'$t_{pulse}$ = 3600 \n $t_{off}$ = 60s', bbox=dict(facecolor='white', edgecolor='k'), fontsize=12)

# matplotx.ylabel_top("Required TBR", ax=axs)

plt.tight_layout()
plt.savefig("tbr_vs_af.png", dpi=300)
plt.show()
