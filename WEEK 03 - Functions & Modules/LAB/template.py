"""
RECORD CHECK  -  my version
===========================

Name  : Saaimah Zainab
Lane  : Cyber
Date  : 07/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"

def status_of(percent):
    """Return a status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Return the difference and percentage."""
    difference = limit - value
    percent = value / limit * 100
    return difference, percent


# ==================================================================== INPUT
# 2. Ask for your three values.

label = input("Enter the record name: ")
value = float(input("Enter the value: "))
limit = float(input("Enter the limit: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.

difference, percent = check(value, limit)
status = status_of(percent)


# =================================================================== OUTPUT
# 4. Print the report.

def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {label}")
    print("=" * 34)
    print(f" Used       : {value:>8.2f}")
    print(f" Total      : {limit:>8.2f}")
    print(f" Free       : {difference:>8.2f}")
    print(f" Percent    : {percent:>7.2f} %")
    print(f" Status     : {status:>8}")
    print("=" * 34)

print_report(label, value, limit, difference, percent, status)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
