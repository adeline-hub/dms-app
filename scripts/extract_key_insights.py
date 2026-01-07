import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
from utils.llm import ask
from utils.chunker import chunk_text

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
args = parser.parse_args()

BASE = Path(f"projects/{args.project}")
DOCS = BASE / "standardized/docs"
OUT = BASE / "insights/key_insights.md"

insights = []

for doc in DOCS.glob("*.md"):
    text = doc.read_text(encoding="utf-8")
    for chunk in chunk_text(text):
        prompt = f"""
Extract investment‑relevant insights from the text below.

Focus on:
- Market
- Regulation
- Business model
- Risks

RULES:
- Group insights by topic
- After EACH bullet, add citation in brackets
- Citation must be the source filename

Format exactly:
- Insight text (Source: filename.pdf)

Text:
{chunk}
"""
        insights.append(ask(prompt))

OUT.write_text(
    "# Key Insights\n\n" + "\n\n".join(insights),
    encoding="utf-8"
)

print("Insights extracted from real documents")