# Import dependencies
import os
import csv
#Create filepath for input and output
budget_csv_path = os.path.join("budget_data.csv")
result_txt_path = os.path.join("results.txt")

print("Financial Analysis")
print("-------------------------------------")
#Declaring varibales
date,revenuechange = ([] for i in range(2))
revenue_change_list = []
total_months = 0
prev_revenue = 0
total_revenue= 0
#Read the file 
with open(budget_csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip the head
    header = next(csvreader)
#for loop
    for row in csvreader:
# total month 
        total_months += 1
# total revenue
        total_revenue += int(row[1])
# revenue change
        revenue_change = int(row[1])-prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list += [revenue_change]
# add date and revenue change to the definded list
        date.append(row[0])
        revenuechange.append([revenue_change])
    length = int(len(revenue_change_list)-1)
    average_change = round(sum(revenue_change_list[1:])/length,2)
    greatest_increase = max(revenue_change_list)
    greatest_decrease = min(revenue_change_list)
    index1 = revenue_change_list.index(max(revenue_change_list))
    index2 = revenue_change_list.index(min(revenue_change_list))
    
    
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_revenue}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {date[index1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {date[index2]} (${greatest_decrease})")
with open(result_txt_path, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Financial Analysis for: " + budget_csv_path],
        ["-" * 50],
        [f"Total Months: {total_months}"],
        [f"Total: ${total_revenue}"],
        [d"Average Change: ${average_change}"]
        [f"Greatest Increase in Profits: {date[index1]} (${greatest_increase})"],
        [f"Greatest Decrease in Profits: {date[index2]} (${greatest_decrease})"]
    ])
        
    
       