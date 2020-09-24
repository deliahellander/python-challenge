# read in cvs file (steps taken from class activities)
import os
import csv
csvpath = r"/Users/deliahellander/Documents/Data Science Bootcamp RU/python-challenge/python-challenge/PyPoll/Resources/election_data.csv"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
   
    #create list variables
    voter_id = []
    county = []
    candidate = []
    khan = []
    correy = []
    li = []
    otooley = []

    # create lists for the columns from the csv
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    print(len(voter_id))

    #seperate out the votes by candidate
    for candidate_ in candidate:
        if candidate_ == "Khan":
            khan.append(candidate)
            khan_vote_percentage = len(khan)/len(voter_id)
        if candidate_ == "Correy":
            correy.append(candidate)
            correy_vote_percentage = len(correy)/len(voter_id)
        if candidate_ == "Li":
            li.append(candidate)
            li_vote_percentage = len(li)/len(voter_id)
        if candidate_ == "O'Tooley":
            otooley.append(candidate)
            otooley_vote_percentage = len(otooley)/len(voter_id)

    #print("{:.0%}".format(khan_vote_percentage))
    percentage_khan = "{:.0%}".format(khan_vote_percentage)
    percentage_correy = "{:.0%}".format(correy_vote_percentage)
    percentage_li = "{:.0%}".format(li_vote_percentage)
    percentage_otooley = "{:.0%}".format(otooley_vote_percentage)

    



#Summary of findings
print("Election Results")
print("------------------------------------------------")
print(f"Total Votes: {len(voter_id)}")
print("------------------------------------------------")
print(f"Khan: {percentage_khan} ({len(khan)})")
print(f"Correy: {percentage_correy} ({len(correy)})")
print(f"Li: {percentage_li} ({len(li)})")
print(f"O'Tooley: {percentage_otooley} ({len(otooley)})")
print("------------------------------------------------")
print("Winner: Khan")

#create an output csv with findings 
# Specify the file to write to
output_path = os.path.join("PyPollFindings.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as file:

    # Write in rows
    file.write("Election Results")
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(voter_id)}")
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write(f"Khan: {percentage_khan} ({len(khan)})")
    file.write("\n")
    file.write(f"Correy: {percentage_correy} ({len(correy)})")
    file.write("\n")
    file.write(f"Li: {percentage_li} ({len(li)})")
    file.write("\n")
    file.write(f"O'Tooley: {percentage_otooley} ({len(otooley)})")
    file.write("\n")
    file.write("-----------------------------------------")
    file.write("\n")
    file.write("Winner: Khan")
    file.write("\n")




