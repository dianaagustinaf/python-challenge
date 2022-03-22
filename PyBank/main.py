import os
import csv

#------------------READ CSV-----------------------------   
#Runned with GitBash

csvpath = os.path.join('Resources', 'budget_data.csv')
analysispath = os.path.join('analysis', 'analysis_bank.txt') 

dates = []
profit_losses = []
changes_months = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csvheader = next(csvreader)
    #print(f"Header: {csvheader}")

    for row in csvreader:
        
        dates.append(row[0])  
        profit_losses.append(int(row[1]))


#------------------ANALYSIS-----------------------------   

def bank_analysis(filepath, dates, nums, changes_m):      

    analysis = open(filepath, 'w') 
    # print(dates)
    # print(nums)
    analysis.write(" Result")
    analysis.write("\n Financial Analysis")
    analysis.write("\n----------------------------")

# The total number of months included in the dataset

    analysis.write("\n Total Months: " + str(len(dates)))

# The net total amount of "Profit/Losses" over the entire period

    net_total = sum(nums)
    analysis.write("\n Total: $" + str(net_total))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

    changes(nums,changes_m)

    avg_change = average(changes_m)

    analysis.write("\n Average Change: $" + str(avg_change))


# The greatest increase in profits (date and amount) over the entire period

    max_profit = -9999999
    index = 0
    for x in range(0,len(changes_m)):
        if changes_m[x] > max_profit:
            max_profit = changes_m[x]
            index = x+1
    max_profit_str = f'{dates[index]} (${max_profit})'

    
    analysis.write("\n Greatest Increase in Profits: " + max_profit_str)

# The greatest decrease in profits (date and amount) over the entire period

    min_profit = 9999999
    index = 0
    for x in range(0,len(changes_m)):
        if changes_m[x] < min_profit:
            min_profit = changes_m[x]
            index = x+1
    min_profit_str = f'{dates[index]} (${min_profit})'

    
    analysis.write("\n Greatest Decrease in Profits: " + min_profit_str)


    analysis.close()

#------------------FUNCTIONS-----------------------------   

def sum(nums):
    count= 0
    for i in nums:
        count=count+i
    return count

def average(nums):
    num = sum(nums)/len(nums) 
    return(round(num,2))

def changes(listData, listResults):
    for i in range(1,len(listData)):
        change = listData[i]-listData[i-1]
        listResults.append(change)
    

#------------------RESULT-----------------------------   
 
bank_analysis(analysispath, dates, profit_losses, changes_months) 

#------------------PRINT RESULT-----------------------  

results = open(analysispath, "r")
print(results.read())


# Result
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


# Disclaimer: this file was run with Git Bash. 
# From the VS Code terminal it needs another path.
# (add PyBank folder)