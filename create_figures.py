
# ==========================================
# IMPORT LIBRARIES
# ==========================================

from pathlib import Path
import pymupdf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ==========================================
# PROJECT FILE PATHS
# ==========================================

# Automatically find the folder containing
# the current Python script
root = Path(__file__).resolve().parent

# Define the source and output directories
sources = root / "sources"
assets = root / "assets"

# Create the assets folder if it doesn't exist
assets.mkdir(parents=True, exist_ok=True)

# Path to your supplementary material
supplementary_pdf = sources / "supplementary.pdf"

# Check that the source PDF exists
if not supplementary_pdf.is_file():
    raise FileNotFoundError(
        f"Supplementary PDF not found:\n"
        f"{supplementary_pdf}\n\n"
        "Place supplementary.pdf inside the "
        "'sources' folder of your project."
    )

# Open the supplementary material
pdf = pymupdf.open(str(supplementary_pdf))

# Use vector drawing for the data chart; all values from manuscript Table 2 (a)/(b)
assets_names=['Bitcoin','S&P 500 ETF','Gold ETF','S&P US REIT','Yen Trust']
absolute=np.array([2.7340,2.1825,5.3194,3.1620,5.0034])
realized=np.array([2.6086,2.2511,7.0969,2.9290,5.6236])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'axes.linewidth':0.9, 'pdf.fonttype':42})
fig, ax=plt.subplots(figsize=(11.2,5.0),dpi=160)
y=np.arange(len(assets_names));h=0.34
b1=ax.barh(y-h/2, absolute, height=h, color='#BE1E2D', label='Absolute return $|y_t|$')
b2=ax.barh(y+h/2, realized, height=h, color='#596673', label='Realized volatility')
ax.set_yticks(y,assets_names)
ax.invert_yaxis()
ax.set_xlim(0,8.1)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.set_xlabel('Diebold–Mariano test statistic (positive favors HF)',labelpad=9)
ax.grid(axis='x',alpha=0.18);ax.set_axisbelow(True)
for bb in [b1,b2]:
 for rect in bb:
  v=rect.get_width();ax.text(v+0.13,rect.get_y()+rect.get_height()/2,f'{v:.2f}',va='center',ha='left',fontsize=12.5,color='#243343')


# Legend centered above the plotting area
ax.legend(
    loc="lower center",
    bbox_to_anchor=(0.5, 1.02),
    ncol=2,
    frameon=False,
    fontsize=12
)

# Give the legend room
fig.subplots_adjust(top=0.83)


# Leave additional space for the legend
fig.subplots_adjust(bottom=0.28)

ax.spines[['right','top']].set_visible(False)
fig.subplots_adjust(left=0.19,right=0.99,bottom=0.19,top=0.98)
fig.savefig(assets/'dm_beta_vs_hf.pdf',bbox_inches='tight')
fig.savefig(assets/'dm_beta_vs_hf.png',bbox_inches='tight',dpi=180)
plt.close(fig)
# Supplementary Table A1: excess kurtosis of demeaned daily returns
kurt=[15.8254,13.4914,5.0618,22.4787,4.5951]
fig, ax=plt.subplots(figsize=(10.0,3.7),dpi=160)
y=np.arange(5)
ax.barh(y,kurt,color=['#BE1E2D','#667382','#667382','#BE1E2D','#667382'],height=0.58)

# Add horizontal space for the value labels
ax.set_xlim(0, 8.5)

# Keep the values outside the bars
for bars in (bars_absolute, bars_rv):
    ax.bar_label(
        bars,
        fmt="%.2f",
        padding=4,
        fontsize=11
    )

ax.set_yticks(y,assets_names)
ax.invert_yaxis()
ax.set_xlim(0,27)
for i,v in enumerate(kurt):ax.text(v+0.35,i,f'{v:.2f}',va='center',fontsize=12)
ax.set_xlabel('Excess kurtosis (Supplementary Table A1)',labelpad=7)
ax.spines[['right','top']].set_visible(False)
ax.grid(axis='x',alpha=0.14);ax.set_axisbelow(True)
fig.subplots_adjust(left=0.19,right=0.98,bottom=0.2,top=0.97)
fig.savefig(assets/'excess_kurtosis.pdf',bbox_inches='tight')
plt.close(fig)
