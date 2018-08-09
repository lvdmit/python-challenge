import os
import csv
budget_csv = 'budget_data.csv'

#The total number of months is equal to the number of rows - headerline
total_months = sum(1 for line in open(budget_csv)) - 1

change = 0
total_change = 0
line = 0
changes =[]

csvfile = open(budget_csv)
csvreader = csv.reader(csvfile, delimiter=",")
next(csvreader)   
for row in csvreader:
    total = int(row[1])
    previous_revenue = int(row[1])
    #print(previous_revenue)
    for row in csvreader:
        change = int(row[1]) - previous_revenue
        #print(previous_revenue)
        changes.append(change)
        previous_revenue = int(row[1])
        #print(change)
        total += int(row[1])

max_value = max(changes)
max_index = changes.index(max_value)
min_value = min(changes)
min_index = changes.index(min_value)
#print(max_value, max_index, min_value, min_index)
#print(changes)
total_change = sum(changes) 
#print(total_change)
average_change = total_change/len(changes) 
#print(average_change)
print ("Financial Analysis")
print("----------------------")
print (f'Total Months: {total_months}')
print(f'Total: ${total}') 
print(f"Average  Change: ${average_change}") 

csvfile = open(budget_csv)
csvreader = csv.reader(csvfile, delimiter=",")
next(csvreader)
for row in csvreader:
    line += 1
    #index + 2 because we skipped 2 lines before
    if line == max_index + 2:
        print("Greatest Increase in Profits: {}({})".format(row[0], max_value))
    if line == min_index + 2:
        print("Greatest Decrease in Profits: {}({})".format(row[0], min_value))    

   





