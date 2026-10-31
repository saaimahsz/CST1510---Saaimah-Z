"""
RECORD CHECK  -  my version
===========================

Name  : Saaimah Zainab
Lane  : Cyber
Date  : 12/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). Give each a one-line docstring.

def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status

def print_report(label, value, limit, difference, percent, status):
    """"Print a report for one record."""
    print("-------------------------------")
    print(f"RECORD CHECK - {label}")
    print(f"Used:       {value:8.2f}")
    print(f"Total:      {limit:8.2f}")
    print(f"Free:       {difference * -1:8.2f}")
    print(f"Percent:    {percent:7.2f}%")
    print(f"Status:     {status}")
    print("-------------------------------")

def load_records(path):
    """Load records from a file and return a list of dictionaries."""
    records = []

    try:
        with open(path, "r") as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
    except FileNotFoundError:
        print(f"{path} not found")
        return []

    return records


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:

from pathlib import Path

records = load_records(Path(__file__).resolve().parent / "cyber_records.txt")
print(records)


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.

over_limit_count = 0

with open(Path(__file__).resolve().parent / "results.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )
        
        print_report(
            record["label"],
            record["value"],
            record["limit"],
            difference,
            percent,
            status
        )

        
        f.write(f'{record["label"]}, {status}\n')

        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Records over limit: {over_limit_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
