import numpy as np
import matplotlib.pyplot as plt
import matplotx
import matplotlib.cm as cm
from matplotlib.colors import Normalize, LogNorm


def eta_f_f_b_to_colour(eta_f_f_b):
    """Returns a colour as a blue gradient"""
    norm = LogNorm(vmin=0.01, vmax=max(eta_f_f_b_values))
    return cm.Blues(norm(eta_f_f_b))


eta_f_f_b_values = [0.5, 1, 2, 5]  # %

plt.figure(figsize=(6.4, 3.8))
for eta_f_fb in eta_f_f_b_values:
    data = np.genfromtxt(
        f"data/t_blanket/eta_f x f_b = {eta_f_fb:.1f}%.csv", delimiter=",", names=True
    )
    tau_blanket = data["t_blanket_h"]
    blanket_inv = data["I_blanket_g"]
    plt.plot(
        tau_blanket,
        blanket_inv,
        label="TBE = " + f"{eta_f_fb:.1f}%",
        color=eta_f_f_b_to_colour(eta_f_fb),
    )
plt.ylim(bottom=0)
plt.xlim(left=0, right=240)

plt.ylabel("Blanket inventory (g)")
plt.xlabel(r"Blanket residence time $\tau_\mathrm{BZ}$ (h)")
matplotx.line_labels()
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.tight_layout()
plt.savefig("blanket_inv_vs_tau_bz.pdf")
plt.show()
#
