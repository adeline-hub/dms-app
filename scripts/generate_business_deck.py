import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
from utils.llm import ask

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
args = parser.parse_args()

BASE = Path(f"projects/{args.project}")
MEMO = BASE / "memo"
OUT = BASE / "deck/deck.md"
OUT.parent.mkdir(exist_ok=True)

memo_text = ""
for f in sorted(MEMO.glob("*.md")):
    memo_text += f.read_text(encoding="utf-8") + "\n"

financial_summary = ""
summary_path = BASE / "financial/summary.json"
if summary_path.exists():
    financial_summary = summary_path.read_text()

prompt = f"""
Create a business / investment deck in Markdown.

Rules:
- Use slide titles with '#'
- Bullet points only
- 1 slide per section
- Clear, executive tone

Content:
{memo_text}
Financial Summary:
{financial_summary}
"""

deck_md = ask(prompt)
OUT.write_text(deck_md, encoding="utf-8")

print("Business deck markdown generated")