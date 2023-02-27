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


plt.rcParams["font.size"] = "16"

symbols = [
    "AF",
    "$\mathrm{TBE}$",
    r"$f_\mathrm{dir}$",
    r"$\tau_\mathrm{BZ}$",
    r"$\eta_\mathrm{TES}$",
    "$t_p$",
    r"$t_\mathrm{res}$",
    "$t_d$",
]

params = ["AF", "eta_f_f_b", "f_dir", "tau_bl", "eta_TES", "t_p", "t_res", "t_d"]
means = [0.75, 2.50e-2, 0.5, 12.5, 0.7, 6.5, 24, 6]
sigmas = [0.25, 2.5e-2, 0.5, 11.5, 0.3, 5.5, 24, 5]
symbols = [
    "AF",
    "$\mathrm{TBE}$",
    r"$f_\mathrm{dir}$",
    r"$\tau_\mathrm{BZ}$",
    r"$\eta_\mathrm{TES}$",
    "$t_p$",
    r"$t_\mathrm{res}$",
    "$t_d$",
]
sensitivity_index_coeffs = []
colours = []

metric = "TBR"

designs = ['ARC', 'STEP EBB', 'STEP Li']
data = np.genfromtxt(f"data/RIC_TBR_vs_designs.csv", delimiter=",")
relative_sensitivity_indexes_vals = data

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
    # (l,) = plt.plot(norm_x, norm_y, label=symbols[i], marker='.')
    # colours.append(l.get_color())
sum_indexes = sum([abs(ic) for ic in sensitivity_index_coeffs])
relative_sensitivity_indexes = [ic / sum_indexes for ic in sensitivity_index_coeffs]

fig, ax = plt.subplots()
height = 0.3
sorted_symbols = [x for _, x in sorted(zip(relative_sensitivity_indexes, symbols))]
y = np.arange(len(symbols))
ax.barh(y+height, width=sorted(relative_sensitivity_indexes_vals[:,0]),  height=height,
    align="edge", color='tab:blue')  
ax.barh(y, width=sorted(relative_sensitivity_indexes_vals[:,1]),  height=height,
    align="edge", color='tab:orange')  
ax.barh(y-height, width=sorted(relative_sensitivity_indexes_vals[:,2]),  height=height,
    align="edge", color='tab:green')  
ax.set_yticks(y+height)
ax.set_yticklabels(sorted_symbols)
plt.xlabel("RIC")

plt.grid(True, which="major", axis="x")
plt.gca().set_axisbelow(True)
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.gca().spines.bottom.set_visible(False)
plt.gca().spines.left.set_visible(False)
plt.gca().tick_params(axis="both", which="both", length=0)
plt.legend(designs)
plt.title('TBR$_r$')
plt.tight_layout()
plt.savefig('TBR_RIC_vs_design.pdf')

# Startup inventory

mertic = 'I_st'
data = np.genfromtxt(f"data/RIC_startup_vs_designs.csv", delimiter=",")
relative_sensitivity_indexes_vals = data

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
    # (l,) = plt.plot(norm_x, norm_y, label=symbols[i], marker='.')
    # colours.append(l.get_color())
sum_indexes = sum([abs(ic) for ic in sensitivity_index_coeffs])
relative_sensitivity_indexes = [ic / sum_indexes for ic in sensitivity_index_coeffs]

fig, ax = plt.subplots()
height = 0.3
sorted_symbols = [x for _, x in sorted(zip(relative_sensitivity_indexes, symbols))]
y = np.arange(len(symbols))
ax.barh(y+height, width=sorted(relative_sensitivity_indexes_vals[:,0]),  height=height,
    align="edge", color='tab:blue')  
ax.barh(y, width=sorted(relative_sensitivity_indexes_vals[:,1]),  height=height,
    align="edge", color='tab:orange')  
ax.barh(y-height, width=sorted(relative_sensitivity_indexes_vals[:,2]),  height=height,
    align="edge", color='tab:green')  
ax.set_yticks(y+height)
ax.set_yticklabels(sorted_symbols)
plt.xlabel("RIC")

plt.grid(True, which="major", axis="x")
plt.gca().set_axisbelow(True)
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.gca().spines.bottom.set_visible(False)
plt.gca().spines.left.set_visible(False)
plt.gca().tick_params(axis="both", which="both", length=0)
plt.legend(designs)
plt.title('I$_{st}$')
plt.tight_layout()
plt.savefig('startup_RIC_vs_design.pdf')