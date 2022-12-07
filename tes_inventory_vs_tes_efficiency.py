import numpy as np
import matplotlib.pyplot as plt
import matplotx


eta_f_f_b_values = [0.5, 1, 2, 5]  # %

# create a new figure
plt.figure(figsize=(6.4, 4.2))

# iterate through etaf fb values
for eta_f_f_b in eta_f_f_b_values:

    # fetch csv data with numpy
    data = np.genfromtxt(
        f"data/TES_eff/eta_f x f_b = {eta_f_f_b:.1f}%.csv", delimiter=",", names=True
    )
    plt.plot(data["eta_TES"], data["I_tes_g"], label=f"{eta_f_f_b:.1f}%")

# add labels
plt.text(x=0.98, y=123, s="$\mathrm{TBE} =$")
plt.xlabel("$\eta_\mathrm{TES}$")
matplotx.ylabel_top("TES inventory (g)")

# Linear yscale should always start at zero
plt.ylim(bottom=0)

# Use inline labelling
matplotx.line_labels()

# remove top and right axis, cause we don't need that junk
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.tight_layout()

# save and show
plt.savefig("tes_inv_vs_tes_efficiency.pdf")
plt.show()
