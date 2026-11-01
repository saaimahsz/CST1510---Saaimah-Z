"""
RECORD CHECK  -  my version
===========================

Name  : Saaimah Zainab
Lane  : Cyber
Date  : 26/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).


import pandas as pd

from pathlib import Path

csv_path = Path(__file__).resolve().parent / "login_records.csv"
df = pd.read_csv(csv_path)

print("Rows immediately after loading:", len(df))
print(df.head())


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100
    else "WARNING" if p >= 90
    else "OK"
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df[df["status"] != "OK"])
print(df.groupby("status").size())

df.to_csv("login_report.csv", index=False)

import matplotlib.pyplot as plt

df["status"].value_counts().plot(kind="bar")

plt.title("Login Status Counts")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("login_status_counts.png")
plt.show()


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case
