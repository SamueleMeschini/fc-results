import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

eta_f_f_b_values = [0.5, 1, 2, 5]  # %

fig, axs = plt.subplots(nrows=1, ncols=1, sharex=True)

for eta_f_fb in eta_f_f_b_values:
    data = np.genfromtxt(
        f"data/AF/eta_f x f_b = {eta_f_fb:.1f}%.csv", delimiter=",", names=True
    )
    plt.plot(
        data["AF"],
        data["TBR"],
        label="TBE = " + f"{eta_f_fb:.1f}%",
        marker=".",
    )
plt.vlines([94,97], [1.,1.], [1.38,1.38], colors='k', linestyles='--')
axs.set_xlabel(r"Availability Factor (%)")

matplotx.line_labels(axs, fontsize=10)
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
axs.grid(which="major", axis="y", alpha=0.1)
axs.set_ylim(1,1.4)
plt.text(77,1.35,'$t_{pulse}$ = 1800s \n $t_{off}$ = 120s', bbox=dict(facecolor='white', edgecolor='k'), fontsize=10)
plt.text(99,1.3,'$t_{pulse}$ = 3600 \n $t_{off}$ = 60s', bbox=dict(facecolor='white', edgecolor='k'), fontsize=10)

matplotx.ylabel_top("Required TBR", ax=axs)

plt.tight_layout()
plt.savefig("tbr_vs_af.pdf")
plt.show()
