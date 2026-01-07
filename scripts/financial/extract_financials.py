import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import argparse
import pandas as pd
import json

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
args = parser.parse_args()

BASE = Path(f"projects/{args.project}")
RAW = BASE / "raw_docs"
OUT = BASE / "financial"
OUT.mkdir(exist_ok=True)

xlsx = next((f for f in RAW.iterdir() if f.suffix == ".xlsx"), None)
if not xlsx:
    raise Exception("No financial model found")

summary = pd.read_excel(xlsx, sheet_name="Summary")

def get(metric, year):
    row = summary[summary.iloc[:, 0] == metric]
    if row.empty:
        return None
    return float(row[year]) if pd.notna(row[year]).any() else None

data = {
    "revenue": {
        "year_1": get("Revenue", "Year 1"),
        "year_2": get("Revenue", "Year 2"),
        "year_3": get("Revenue", "Year 3"),
    },
    "ebitda": {
        "year_1": get("EBITDA", "Year 1"),
        "year_2": get("EBITDA", "Year 2"),
        "year_3": get("EBITDA", "Year 3"),
    }
}

(OUT / "summary.json").write_text(json.dumps(data, indent=2))
print("Financials extracted from template")