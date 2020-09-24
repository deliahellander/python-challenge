# read in cvs file (steps taken from class activities)
import os
import csv
csvpath = r"/Users/deliahellander/Documents/Data Science Bootcamp RU/RUT-SOM-DATA-PT-09-2020-U-C/01-Lesson-Plans/03-Python/python-challenge/PyBank/Resources/budget_data.csv"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    month = []
    profit = []
    # create lists for the columns from the csv
    for row in csvreader:
        month.append(row[0])
        profit.append(row[1])
    print(len(month))
 
    
    #finding net profit using map funtion to iterate
    profit_=map(int, profit)
    net_profit =(sum(profit_))
    print(net_profit)

    average_change = []

    #using i loop to find average change
    #Using length of profit list as end of range
    for i in range(len(profit)-1):
        #creating a new list for finding average change
        profit_change = int(profit[i+1]) - int(profit[i])
        average_change.append(profit_change)
        final_average_change = sum(average_change)/len(average_change)
    print(final_average_change)
    
    #using average change list to find the greatest increase/decrease amt & date
    greatest_profit_increase = max(average_change)
    greatest_profit_decrease = min(average_change)
    #assigning greatest increase/decrease with its month/row location
    greatest_profit_increase_date = average_change.index(max(average_change)) + 1
    greatest_profit_decrease_date = average_change.index(min(average_change)) + 1
    
    print(greatest_profit_increase)
    print(greatest_profit_decrease)
    print(greatest_profit_increase_date)
    print(greatest_profit_decrease_date)

#Summary of Findings
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: $ {net_profit}")
print(f"Average Change: $ {round(final_average_change,2)}")
print(f"Greatest Increase in Profits: {month[greatest_profit_increase_date]} + (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {month[greatest_profit_decrease_date]} + (${greatest_profit_decrease})")

#create an output csv with findings 
# Specify the file to write to
output_path = os.path.join("PyBankFindings.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

    # Write in rows
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(month)}")
    file.write("\n")
    file.write(f"Total: $ {net_profit}")
    file.write("\n")
    file.write(f"Average Change: $ {round(final_average_change,2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {month[greatest_profit_increase_date]} + (${greatest_profit_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {month[greatest_profit_decrease_date]} + (${greatest_profit_decrease})")
    file.write("\n")