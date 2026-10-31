# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

from pathlib import Path

file_path = Path(__file__).resolve().parents[2] / "DEMO" / "records.txt"

with open(file_path) as f:
    print(f.read())
