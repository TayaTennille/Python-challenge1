import os
import csv

csvpath = os.path.join('..', Resources,"budget_data")
print(csvpath)

with open(csvpath) as csvfile:
    csvreader =csv.reader(budget_data, delimiter= ',')
    print (csvreader)

    # Path to the budget data file
budget_data_path = os.path.join("budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
months = []

# Read the budget data file
with open(budget_data_path, 'r') as budget_file:
    csvreader = csv.reader(budget_file, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        # Count total months
        total_months += 1
        
        # Calculate net total profit/loss
        net_total += int(row[1])
        
        # Track profit changes
        if total_months > 1:
            profit_change = int(row[1]) • previous_profit
            profit_changes.append(profit_change)
            months.append(row[0])
        
        previous_profit = int(row[1])

# Calculate average change
average_change = round(sum(profit_changes) / len(profit_changes), 2)

# Find greatest increase and decrease in profits
greatest_increase = max(profit_changes)
greatest_increase_index = profit_changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index + 1]
greatest_decrease = min(profit_changes)
greatest_decrease_index = profit_changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index + 1]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export the results to a text file
output_path = "financial_analysis.txt"
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")




import os
import csv

# Path to the election data file
election_data_path = os.path.join("election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the election data file
with open(election_data_path, 'r') as election_file:
    csvreader = csv.reader(election_file, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        # Count total votes
        total_votes += 1
        
        candidate = row[2]
        
        # Count
                        