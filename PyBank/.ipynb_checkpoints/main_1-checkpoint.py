import os
import csv

budget_csv_path = os.path.join("budget_data.csv")
result_txt_path = os.path.join("results_1.txt")

print("Financial Analysis")
print("-------------------------------------")

date_revenuechange = {}
revenue_change_list = []
total_months = 0
prev_revenue = 0
total_revenue= 0
with open(budget_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        revenue_change = int(row[1])-prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list += [revenue_change]
        date_revenuechange[row[0]] = revenue_change
    
stats = [(value,key) for key, value in date_revenuechange.items()]
length = int(len(revenue_change_list)-1)
average_change = round(sum(revenue_change_list[1:])/length,2)

print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max(stats)[1]} (${max(stats)[0]})")
print(f"Greatest Decrease in Profits: {min(stats)[1]} (${min(stats)[0]})")

with open(result_txt_path, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Financial Analysis for: " + budget_csv_path],
        ["-" * 50],
        [f"Total Months: {total_months}"],
        [f"Total: ${total_revenue}"],
        [f"Greatest Increase in Profits: {max(stats)[1]} (${max(stats)[0]})"],
        [f"Greatest Decrease in Profits: {min(stats)[1]} (${min(stats)[0]})"]
    ])
        

