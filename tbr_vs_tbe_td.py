import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.figure(figsize=(6.4, 3))

for doubling_time in [1, 2, 5]:
    data = np.genfromtxt(
        f"data/t_d/doubling_time = {doubling_time}y.csv", delimiter=",", names=True
    )

    TBE = data["eta_f"] * data["f_b"] * 100

    plt.plot(TBE[::-1], data["TBR"][::-1], label=f"$t_d = {doubling_time}$ y")

# to get labels closer
plt.xlim(right=5)

plt.ylim(1, 1.5)

matplotx.line_labels()

plt.xlabel("TBE (%)")
plt.ylabel("Required TBR")

# remove top and right axis, cause we don't need that junk
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.tight_layout()

plt.savefig("tbr_vs_tbe_td.pdf")

plt.show()
