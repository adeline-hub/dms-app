import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
args = parser.parse_args()

BASE = Path(f"projects/{args.project}")
RAW = BASE / "raw_docs"
OUT = BASE / "financial/charts"
OUT.mkdir(parents=True, exist_ok=True)

financial_file = next(f for f in RAW.iterdir() if f.suffix == ".xlsx")
df = pd.read_excel(financial_file)

plt.figure()
plt.plot(df.iloc[:, 0], df.iloc[:, 1])
plt.title("Revenue Projection")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.savefig(OUT / "revenue.png")

print(" Financial chart generated")