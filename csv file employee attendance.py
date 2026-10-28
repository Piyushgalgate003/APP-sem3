import csv
from collections import defaultdict

totals = defaultdict(int)
names = {}

with open("attendance.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        emp_id = int(row["EmpID"].strip())
        name = row["Name"].strip()
        days = int(row["DaysPresent"].strip())

        names[emp_id] = name
        totals[emp_id] += days

print(f"{'EmpID':<8}{'Name':<12}{'Total Days'}")
for emp_id, days in totals.items():
    print(f"{emp_id:<8}{names[emp_id]:<12}{days}")