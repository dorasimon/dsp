#6

import csv

# Get name list
n = []
with open("faculty.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        n.append(row["name"])
    print(n)
# Get degree & title & email list
dte = []
with open("faculty.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dte.append(row[" degree"])
        dte.append(row[" title"])
        dte.append(row[" email"])
    print(dte)
# Split it by 3
sub_dte = [dte[i:i + 3] for i in range(0, len(dte), 3)]
print(sub_dte)
# Get last name list
def last_name(N):
    return N[N.rfind(" ") + 1:]
ln = []
for name in n:
    ln.append(last_name(name))
print(ln)
# Create a dictionary with last name
d = {}
for key, value in zip(ln, sub_dte):
    d.setdefault(key, []).append(value)
print(d)