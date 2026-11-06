
# ==========================================
# IMPORT LIBRARIES
# ==========================================

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ==========================================
# PROJECT FILE PATHS AND PLOT SETTINGS
# ==========================================

# Find the folder containing this Python script
root = Path(__file__).resolve().parent

# Define the output folder
assets = root / "assets"

# Create the assets folder if it does not exist
assets.mkdir(parents=True, exist_ok=True)

# Set default formatting for the charts
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 14,
    "axes.linewidth": 0.9,
    "pdf.fonttype": 42
})

# Financial assets used in the research
names = [
    "Bitcoin",
    "S&P 500 ETF",
    "Gold ETF",
    "S&P US REIT",
    "Yen Trust"
]

# Chart colors
red = "#BE1E2D"
gray = "#596673"
label_color = "#243343"


# ==========================================
# FIGURE 1: VOLATILITY FORECAST COMPARISON
# Manuscript Table 2(a) and 2(b)
# ==========================================

# Diebold-Mariano test statistics
# Positive values favor HF-Beta-t-EGARCH

absolute = np.array([
    2.7340,
    2.1825,
    5.3194,
    3.1620,
    5.0034
])

realized = np.array([
    2.6086,
    2.2511,
    7.0969,
    2.9290,
    5.6236
])

# Create the chart
fig, ax = plt.subplots(
    figsize=(11.2, 5.0),
    dpi=160
)

# Define bar positions
y = np.arange(len(names))
h = 0.34

# Absolute return bars
bars_absolute = ax.barh(
    y - h / 2,
    absolute,
    height=h,
    color=red,
    label=r"Absolute return $|y_t|$"
)

# Realized volatility bars
bars_rv = ax.barh(
    y + h / 2,
    realized,
    height=h,
    color=gray,
    label="Realized volatility"
)

# Format chart axes
ax.set_yticks(y, labels=names)
ax.invert_yaxis()

# Allow room for numerical labels
ax.set_xlim(0, 8.1)

# Set x-axis increments
ax.xaxis.set_major_locator(
    ticker.MultipleLocator(2)
)

ax.set_xlabel(
    "Diebold-Mariano Test Statistic (positive favors HF)",
    labelpad=9
)

# Add vertical gridlines
ax.grid(axis="x", alpha=0.18)
ax.set_axisbelow(True)

# Remove unnecessary chart borders
ax.spines[["right", "top"]].set_visible(False)

# Add numerical labels to both bar series
for bars in (bars_absolute, bars_rv):
    ax.bar_label(
        bars,
        fmt="%.2f",
        padding=4,
        fontsize=11.5,
        color=label_color
    )

# Position legend above the chart
ax.legend(
    loc="lower center",
    bbox_to_anchor=(0.5, 1.02),
    ncol=2,
    frameon=False,
    fontsize=12
)

# Set chart margins once
fig.subplots_adjust(
    left=0.20,
    right=0.97,
    bottom=0.20,
    top=0.81
)

# Save figures
fig.savefig(
    assets / "dm_beta_vs_hf.pdf",
    bbox_inches="tight"
)

fig.savefig(
    assets / "dm_beta_vs_hf.png",
    bbox_inches="tight",
    dpi=180
)

plt.close(fig)


# ==========================================
# FIGURE 2: EXCESS KURTOSIS
# Supplementary Material Table A1
# ==========================================

# Excess kurtosis for the five assets
kurtosis = np.array([
    15.8254,
    13.4914,
    5.0618,
    22.4787,
    4.5951
])

# Create the chart
fig, ax = plt.subplots(
    figsize=(10.0, 3.7),
    dpi=160
)

y = np.arange(len(names))

# Create horizontal bars
bars_kurtosis = ax.barh(
    y,
    kurtosis,
    color=[red, gray, gray, red, gray],
    height=0.58
)

# Format chart axes
ax.set_yticks(y, labels=names)
ax.invert_yaxis()

# Allow room for kurtosis values and labels
ax.set_xlim(0, 27)

# Set x-axis increments
ax.xaxis.set_major_locator(
    ticker.MultipleLocator(5)
)

ax.set_xlabel(
    "Excess kurtosis (Supplementary Table A1)",
    labelpad=7
)

# Add gridlines
ax.grid(axis="x", alpha=0.14)
ax.set_axisbelow(True)

# Remove unnecessary borders
ax.spines[["right", "top"]].set_visible(False)

# Add numerical values to the bars
ax.bar_label(
    bars_kurtosis,
    fmt="%.2f",
    padding=4,
    fontsize=11.5,
    color=label_color
)

# Adjust margins
fig.subplots_adjust(
    left=0.22,
    right=0.97,
    bottom=0.23,
    top=0.97
)

# Save figures
fig.savefig(
    assets / "excess_kurtosis.pdf",
    bbox_inches="tight"
)

fig.savefig(
    assets / "excess_kurtosis.png",
    bbox_inches="tight",
    dpi=180
)

plt.close(fig)

print("Figures generated successfully in:", assets)
