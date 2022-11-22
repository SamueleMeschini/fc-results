import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import numpy as np


t_p_values = [1, 4, 12]  # h
doubling_time_values = [2, 5]  # years

# plotting
def t_p_to_colour(t_p):
    """Returns a colour as a blue gradient"""
    # the minimum is not 0 otherwise tp=1h is almost white
    norm = Normalize(vmin=-10, vmax=max(t_p_values))
    return cm.Blues(norm(t_p))


fig, axs = plt.subplots(nrows=2, ncols=2, sharex=True, sharey="row")

for row_index, metric in enumerate(["TBR", "I_startup_kg"]):
    row_plots = axs[row_index]
    for col_index, t_d in enumerate(doubling_time_values):

        folder = f"data/eta_fxf_b_td{t_d}y"

        plot = row_plots[col_index]
        plt.sca(plot)
        for tp in t_p_values:
            filename = folder + f"/IFC processing time = {tp}h.csv"
            data = np.genfromtxt(filename, delimiter=",", names=True)
            eta_f_f_b = data["eta_f"] * data["f_b"]  # no need to multiply by 100 here

            plt.plot(
                eta_f_f_b,
                data[metric],
                label=f"$t_p$ = {tp} h",
                color=t_p_to_colour(tp),
            )
            # inline label
            plt.annotate(
                f"$t_p$ = {tp} h  ",
                (eta_f_f_b[-1], data[metric][-1]),
                ha="right",
                va="center",
                color=t_p_to_colour(tp),
            )

# format axes
for ax in axs[1]:
    ax.set_xscale("log")
    ax.set_xlabel("$\eta_f \ f_b$")
    ax.get_xaxis().set_major_formatter(PercentFormatter(1.0))
    # see https://stackoverflow.com/questions/31357611/format-y-axis-as-percent

axs[0][0].set_ylim(bottom=1)
axs[1][0].set_ylim(bottom=0)
axs[0][0].set_xlim(left=0.02 / 100)

axs[0][0].set_ylabel("Required TBR")
axs[1][0].set_ylabel("Startup inventory (kg)")

# add subtitles
for i, t_d in enumerate(doubling_time_values):
    axs[0][i].set_title(f"$t_d = $ {t_d} y")


# to have a legend for all of them, uncomment the following:
# handles, labels = axs[1][1].get_legend_handles_labels()
# fig.legend(
#     handles[::-1], labels[::-1], loc="center right"
# )  # [::-1] to have them in reverse order

# remove top and right axis
for row in axs:
    for ax in row:
        ax.spines.right.set_visible(False)
        ax.spines.top.set_visible(False)

plt.tight_layout()

plt.savefig("tbr_startup_inv_vs_eta_f_f_b.pdf")
plt.show()
