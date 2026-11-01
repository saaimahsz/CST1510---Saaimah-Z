# =================================
# PROJECT: LOGIN ATTEMPTS REPORT
# =================================

import pandas as pd

import matplotlib.pyplot as plt

# Load the login attempts data
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "login_attempts.csv"
df = pd.read_csv(csv_path)

# Inspect the data
print(df.head())
print(df.dtypes)
print(len(df))


# Filter sessions with 3 or more failed attempts
suspicious_sessions = df[df["failed"] >= 3]

print(suspicious_sessions)


# Calculate total failed attempts per IP address
failed_by_ip = df.groupby("ip")["failed"].sum()


# Sort from highest to lowest
failed_by_ip = failed_by_ip.sort_values(ascending=False)

print(failed_by_ip)


# Flag suspicious login sessions
df["suspicious"] = df["failed"].apply(
    lambda x: "True" if x >= 3 else "False"
)

print(df[["ip", "failed", "suspicious"]])


# Chart of total failed attempts per IP address
failed_by_ip.plot(kind="bar")

plt.title("Failed Login Attempts per IP")
plt.xlabel("IP Address")
plt.ylabel("Total Failed Attempts")
plt.tight_layout()

plt.savefig("failed_attempts_by_ip.png")
plt.show()


# Save suspicious login sessions to a CSV file
flagged_ips = df[df["suspicious"] == "True"]
flagged_ips.to_csv("flagged_ips.csv", index=False)

print(flagged_ips)


# Investigation:
# I would investigate 10.0.0.12 first because it had 8 failed login attempts in a single session.
# This is worth investigating because repeated failures in one session may indicate a possible brute-force attempt.
