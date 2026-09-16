import csv
import json

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    records = []

    for row in reader:
        records.append(row)

with open("students.json", "w") as f:
    json.dump(records, f, indent=4)

print("CSV converted to JSON successfully!")