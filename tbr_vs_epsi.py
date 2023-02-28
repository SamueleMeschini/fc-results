import numpy as np
import matplotlib.pyplot as plt
import matplotx

plt.rcParams["font.size"] = "14"

TBE_values = [0.5, 1, 2, 5]  # %

fig, axs = plt.subplots(nrows=2, ncols=1,sharex=True, figsize=(6.4, 6))

for TBE in TBE_values:
    data = np.genfromtxt(
        f"data/epsi/TBE={TBE:.1f}%.csv", delimiter=",", names=True
    )
    plt.sca(axs[0])
    plt.plot(
        data["epsi"],
        data["TBR_req"],
        label="TBE = " + f"{TBE:.1f}%",
        marker=".",
    )
    plt.sca(axs[1])
    plt.plot(
        data["epsi"],
        data["TBR_req"],
        label="TBE = " + f"{TBE:.1f}%",
        marker=".",)
    

matplotx.ylabel_top("Required TBR", ax=axs[0])
matplotx.ylabel_top("Required \n {:<11}".format('TBR'), ax=axs[1])


for ax in axs:
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    # Use inline labelling
    # matplotx.line_labels(ax)
    ax.grid(which="major", axis="y", alpha=0.1)
    ax.set_xscale('log')
    ax.legend(fontsize=12)


axs[1].set_ylim(1,1.4)
# axs[1].set_ylabel("Required TBR")

axs[1].set_xlabel("Non-radioactive loss fraction $\epsilon$")


plt.tight_layout()
plt.savefig("tbr_vs_epsi.pdf")
plt.show()

# fig, (ax1,ax2) = plt.subplots(2,1,sharex=True)

# for TBE in TBE_values:
#     data = np.genfromtxt(
#         f"data/epsi/TBE={TBE:.1f}%.csv", delimiter=",", names=True
#     )
#     ax1.plot(
#         data["epsi"],
#         data["TBR_req"],
#         label="TBE = " + f"{TBE:.1f}%",
#         marker=".",
#     )
#     ax2.plot(
#         data["epsi"],
#         data["TBR_req"],
#         label="TBE = " + f"{TBE:.1f}%",
#         marker=".",
#         )
# # matplotx.line_labels(axs, fontsize=10)
# ax1.set_ylim(1.4,7)
# ax2.set_ylim(1,1.2)
# ax2.spines['top'].set_visible(False)
# ax1.spines['bottom'].set_visible(False)
# ax1.xaxis.tick_top()
# ax1.tick_params(labeltop=False)  # don't put tick labels at the top
# ax2.xaxis.tick_bottom()
# d = .015
# kwargs = dict(transform=ax1.transAxes, color='k', clip_on=False)
# ax1.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
# ax1.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

# kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
# ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
# ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# ax2.set_ylabel("Required TBR")
# ax2.grid(which="major", axis="y", alpha=0.1)
# ax1.grid(which="major", axis="y", alpha=0.1)

# ax2.set_xscale('log')
# ax1.legend()
# ax2.set_xlabel("Non-radioactive loss fraction $\epsilon$")

# # matplotx.ylabel_top("Required TBR", ax=axs)

# plt.tight_layout()
# plt.savefig("tbr_vs_epsi.pdf")
# plt.show()