import os
import csv
from operator import itemgetter, attrgetter
election_csv = 'election_data.csv'

#The total number of votes included is equal to the number of rows - headerline
total_votes = sum(1 for line in open('election_data.csv')) - 1
#print(total_votes)
Khan_list = []
Li_list = []
Correy_list = []
Tooley_list = []

csvfile = open(election_csv)
csvreader = csv.reader(csvfile, delimiter=",")
next(csvreader)   
for row in csvreader:
    if row[2] == "Khan":
        Khan_list.append(row[0])
    if row[2] == "Correy":
        Correy_list.append(row[0])
    if row[2] == "O'Tooley":
        Tooley_list.append(row[0])
    if row[2] == "Li":
        Li_list.append(row[0])
Correy_total = len(Correy_list)
Tooley_total = len(Tooley_list)
Khan_total = len(Khan_list)
Li_total = len(Li_list)
#print(len(Li_list))     
#print(Tooley_total)
#print(Khan_total)
#print(Correy_total)
#print(Li_total)

#Percent formatting in print()
Correy_percent = Correy_total/total_votes
Tooley_percent = Tooley_total/total_votes
Khan_percent = Khan_total/total_votes
Li_percent = Li_total/total_votes

votes = [
    ("Correy", Correy_total), 
    ("O'Tooley", Tooley_total), 
    ("Khan", Khan_total), 
    ("Li", Li_total)
    ]
sorted_votes = sorted(votes, key=itemgetter(1), reverse=True)
#print(sorted_votes)

print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print("Khan: {:.3%} ({})".format(Khan_percent, Khan_total))
print("Correy: {:.3%} ({})".format(Correy_percent, Correy_total))
print("Li: {:.3%} ({})".format(Li_percent, Li_total))
print("O'Tooley: {:.3%} ({})".format(Tooley_percent, Tooley_total))
print("--------------------------")
print("Winner: {}".format(sorted_votes[0][0]))
print("--------------------------")
