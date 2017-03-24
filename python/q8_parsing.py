# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open("football.csv") as file:
    reader = csv.DictReader(file)
    Teams = []
    diffGoals = []
    for row in reader:
        Teams.append(row["Team"])
        diffGoals.append(abs(int(row["Goals"]) - int(row["Goals Allowed"])))
    print(Teams)
    print(diffGoals)
    print(Teams[diffGoals.index(min(diffGoals))])
# Another way is to create a dictionary
    d = dict(zip(Teams, diffGoals))
    print(d)
    print(min(d, key = d.get))
# or
    print(min(d.items(), key = lambda x: x[1])[0])