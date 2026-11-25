import csv
import json

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Krishna", 19, "Pune"])
    writer.writerow(["Rahul", 20, "Mumbai"])
    writer.writerow(["Amit", 21, "Delhi"])

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

with open("data.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

print("CSV converted to JSON successfully")