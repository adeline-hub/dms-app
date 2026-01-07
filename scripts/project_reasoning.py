import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import argparse
from utils.llm import ask

parser = argparse.ArgumentParser()
parser.add_argument("--project", required=True)
parser.add_argument("--question", required=True)
args = parser.parse_args()

answer = ask(args.question)
print("\nANSWER:\n", answer)