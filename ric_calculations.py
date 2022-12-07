import numpy as np
import matplotlib.pyplot as plt
import matplotx


def sensitivity_index_coeff(x, y):
    # make sure x is sorted
    sorted_y = [val for _, val in sorted(zip(x, y))]
    sorted_x = sorted(x)

    delta_x = max(sorted_x) - min(sorted_x)
    delta_y = sorted_y[-1] - sorted_y[0]

    mean_x = x.mean()
    mean_y = y.mean()
    return delta_y / delta_x * mean_x / mean_y


# TODO fix issue #1 related to eta_f f_b data

params = ["AF", "eta_f_f_b", "f_dir", "tau_bl", "eta_TES", "t_p", "t_res", "t_d"]
means = [0.75, 2.50e-2, 0.5, 13, 0.7, 6.5, 24, 6]
sigmas = [0.25, 2.5e-2, 0.5, 11, 0.3, 5.5, 24, 5]
symbols = [
    "AF",
    "$\mathrm{TBE}$",
    r"$f_\mathrm{dir}$",
    r"$\tau_\mathrm{bl}$",
    r"$\eta_\mathrm{TES}$",
    "$t_p$",
    r"$t_\mathrm{res}$",
    "$t_d$",
]
sensitivity_index_coeffs = []
colours = []

metric = "TBR"

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(6.4, 6))
plt.sca(axs[0])
# compute ICs
for i, param in enumerate(params):
    data = np.genfromtxt(f"data/1D_sensitivity/{param}.csv", delimiter=",", names=True)
    x = data[param]
    if param == "AF":
        x *= 1 / 100  # from % to fractions, maybe better to change that in the raw data
    y = data[metric]
    ic = sensitivity_index_coeff(x, y)
    sensitivity_index_coeffs.append(ic)
    norm_x = (x - means[i]) / sigmas[i]
    ref_y = y[np.where(np.isclose(norm_x, 0))]
    norm_y = (y) / ref_y
    (l,) = plt.plot(norm_x, norm_y, label=symbols[i])
    colours.append(l.get_color())

plt.xticks(ticks=[-1, 0, 1], labels=["$\mu - \sigma$", "$\mu$", "$\mu + \sigma$"])
plt.ylim(0.98, 1.02)
matplotx.line_labels(ax=plt.gca())
plt.ylabel("Normalised TBR")
plt.tight_layout()
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)

# compute RICs
sum_indexes = sum([abs(ic) for ic in sensitivity_index_coeffs])
relative_sensitivity_indexes = [ic / sum_indexes for ic in sensitivity_index_coeffs]
for param, ric in zip(params, relative_sensitivity_indexes):
    print(f"{param}: RIC = {ric:.2%}")

# plotting
plt.sca(axs[1])
# sort bars
sorted_params = [x for _, x in sorted(zip(relative_sensitivity_indexes, symbols))]
sorted_colours = [x for _, x in sorted(zip(relative_sensitivity_indexes, colours))]
sorted_rics = sorted(relative_sensitivity_indexes)
plt.barh(sorted_params, sorted_rics, color=sorted_colours)
plt.xlabel("RIC")

plt.grid(True, which="major", axis="x")
plt.gca().set_axisbelow(True)

plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.gca().spines.bottom.set_visible(False)
plt.gca().spines.left.set_visible(False)
plt.gca().tick_params(axis="both", which="both", length=0)
plt.tight_layout()

plt.savefig("ric_TBR.pdf")

sensitivity_index_coeffs = []
colours = []

metric = "I_st"

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(6.4, 6))
plt.sca(axs[0])
# compute ICs
for i, param in enumerate(params):
    data = np.genfromtxt(f"data/1D_sensitivity/{param}.csv", delimiter=",", names=True)
    x = data[param]
    if param == "AF":
        x *= 1 / 100  # from % to fractions, maybe better to change that in the raw data
    y = data[metric]
    ic = sensitivity_index_coeff(x, y)
    sensitivity_index_coeffs.append(ic)
    norm_x = (x - means[i]) / sigmas[i]
    ref_y = y[np.where(np.isclose(norm_x, 0))]
    norm_y = (y) / ref_y
    (l,) = plt.plot(norm_x, norm_y, label=symbols[i])
    colours.append(l.get_color())

plt.xticks(ticks=[-1, 0, 1], labels=["$\mu - \sigma$", "$\mu$", "$\mu + \sigma$"])
plt.ylim(top=2.0)
matplotx.line_labels(ax=plt.gca())
plt.ylabel("Normalised startup inventory")
plt.tight_layout()
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)

# compute RICs
sum_indexes = sum([abs(ic) for ic in sensitivity_index_coeffs])
relative_sensitivity_indexes = [ic / sum_indexes for ic in sensitivity_index_coeffs]
for param, ric in zip(params, relative_sensitivity_indexes):
    print(f"{param}: RIC = {ric:.2%}")

# plotting
plt.sca(axs[1])
# sort bars
sorted_params = [x for _, x in sorted(zip(relative_sensitivity_indexes, symbols))]
sorted_colours = [x for _, x in sorted(zip(relative_sensitivity_indexes, colours))]
sorted_rics = sorted(relative_sensitivity_indexes)
plt.barh(sorted_params, sorted_rics, color=sorted_colours)
plt.xlabel("RIC")

plt.grid(True, which="major", axis="x")
plt.gca().set_axisbelow(True)

plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.gca().spines.bottom.set_visible(False)
plt.gca().spines.left.set_visible(False)
plt.gca().tick_params(axis="both", which="both", length=0)
plt.tight_layout()

plt.savefig("ric_startup_inventory.pdf")
plt.show()
