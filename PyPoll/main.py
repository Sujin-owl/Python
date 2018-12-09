#import dependencies
import os
import csv
# set the data path and export file name
election_csv_path = os.path.join("election_data.csv")
file_output = "results.txt"

print("Election Analysis")
print("-"*50)

#set variables
total_votes = 0
candidates_votes = {}
votes_percent = {}
Base = 0
#open the csv file
with open(election_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
#iterate through the row in csv file
    for row in csvreader:
#calculate the total votes
        total_votes += 1
#put the candidates' name and count their votes in the dictionary
        if row[2] in candidates_votes.keys():
            candidates_votes[row[2]] += 1
        else:
            candidates_votes[row[2]] = 1

#iterate through the key and corresponding value in the dictionary
for key,value in candidates_votes.items():
#calculate the vote% 
    percent = round((int(value)/int(total_votes))*100,3)
#put key and value in votes_percent dictionary
    votes_percent[key] = percent
#find out the winner
    if value > Base:
        Winner = key
        Base = value
#print the analysis to the terminal   
print(f"Total Votes: {total_votes}")
print("-"*50)
for key,value in candidates_votes.items():
    print(f"{key}: {votes_percent[key]}00% ({candidates_votes[key]})")
print("-"*50)
print(f"Winner: {Winner}")
print("-"*50)
# open and export the text file with the results
with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates_votes.items():
        file.write(key + ": " + str(votes_percent[key]) + "00% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + Winner + "\n")
    file.write("------------------------------------- \n")