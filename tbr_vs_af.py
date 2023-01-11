import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "12"

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

axs.set_xlabel(r"Availability Factor (%)")

matplotx.line_labels(axs, fontsize=10)
axs.spines['right'].set_visible(False)
axs.spines['top'].set_visible(False)
axs.grid(which="major", axis="y", alpha=0.1)

matplotx.ylabel_top("Required TBR", ax=axs)

plt.tight_layout()
plt.savefig("tbr_vs_af.pdf")
plt.show()
