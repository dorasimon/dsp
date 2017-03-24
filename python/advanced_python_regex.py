# 1

import csv

with open("faculty.csv") as file:
    reader = csv.DictReader(file)
    
# Get the degree column
    d = []
    for row in reader:
        d.append(row[" degree"])
    print(d)
# Get rid of the leading space
    d1 = []
    for degree in d:
        if degree[0] == " ":
            d1.append(degree[1:])
        else:
            d1.append(degree)
    print(d1)
# Get rid of the dots so that the same degree has the same expression
    d2 = []
    for degree in d1:
        if "." in degree:
            d2.append(degree.replace(".", ""))
        else:
            d2.append(degree)
    print(d2)
# List out all the degrees by splitting up those with multiple degrees
    d3 = []
    for degree in d2:
        for i in degree.split():
            d3.append(i)
    print(d3)
# Count how many different degrees there are (As is seen from d4, "0" is not a degree)
    d4 = []
    for i in d3:
        if i not in d4:
            d4.append(i)
    print(d4)
    print(len(d4))
# Count the total of each degree
    d5 = []
    for i in d4:
        d5.append(d3.count(i))
    print(d5)
# Create a dictionary
    print(dict(zip(d4, d5)))

    
# 2

import csv

with open("faculty.csv") as file:
    reader = csv.DictReader(file)
    
# Get the title column
    t = []
    for row in reader:
        t.append(row[" title"])
    print(t)
# Count how many different titles there are ("Assistant Professor is Brostatistics" should be "Assistant Professor of Biostatistics")
    t1 = []
    for title in t:
        if title not in t1:
            t1.append(title)
    print(t1)
    print(len(t1))
# Correct the typo
    t[t.index("Assistant Professor is Biostatistics")] = "Assistant Professor of Biostatistics"
    print(t)
# Count the total of each title
    t2 = []
    for title in t1[:-1]:
        t2.append(t.count(title))
    print(t2)
# Create a dictionary
    print(dict(zip(t1, t2)))

    
# 3 & 4

import csv

with open("faculty.csv") as file:
    reader = csv.DictReader(file)
# Get email list
    e = []
    for row in reader:
        e.append(row[" email"])
    print(e)
# Get domain list 
    def get_domain(a):
        return a[a.index("@") + 1:]
    d = []
    for email in e:
        d.append(get_domain(email))
    print(d)
    print(len(set(d)))
    print(list(set(d)))