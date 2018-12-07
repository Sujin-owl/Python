import os
import csv

election_csv_path = os.path.join("election_data.csv")
result_txt_path = os.path.join("results.txt")

print("Election Analysis")
print("-"*50)


total_votes = 0
candidates_votes = {}
votes_percent = {}
Base = 0
with open(election_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] in candidates_votes.keys():
            candidates_votes[row[2]] += 1
        else:
            candidates_votes[row[2]] = 1


for key,value in candidates_votes.items():
    percent = round((int(value)/int(total_votes))*100,3)
    votes_percent[key] = percent
    if value > Base:
        Winner = key
        Base = value
    
print(f"Total Votes: {total_votes}")
print("-"*50)
for key,value in candidates_votes.items():
    print(f"{key}: {votes_percent[key]}00% ({candidates_votes[key]})")
print("-"*50)
print(f"Winner: {Winner}")
print("-"*50)
with open(result_txt_path, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Electron Analysis for: " + election_csv_path],
        ["-" * 50],
        [f"Total Votes: {total_votes}"],
        ["-"*50],
        [f"{key}: {votes_percent[key]}00% ({candidates_votes[key]})"],
        ["-"*50],
        [f"Winner: {Winner}"],
        ["-"*50]
        
    ])