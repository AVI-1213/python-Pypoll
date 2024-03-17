# importing the module OS and CSV
import os
import csv

# using OS asigning filepath
filepath = os.path.join("..","Resources","budget_data.csv")

# initializing Variables
monthCount = []
PnL = []
totalPnL = 0
changesPnL = []
greatestIncrease = 0
greatestDecrease = 0

# reading from filepath and skipping headers
with open(filepath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader, None)
    
    # for row in csv_reader:
    #     print(row[0:])

# # solution 1: 
#Total number of month & Net total profit & loss

    for row in csv_reader :
        monthCount.append(row[0])
        PnL.append(int(row[1]))

# total number of month count
    totalMonth = len(monthCount)
    # print ("Total Months : ", totalMonth)

# Solution 2 : The net total amount of "Profit/Losses" over the entire period
    totalPnL = sum(PnL)
    # print("Net Total amount of Profit/loss : ", totalPnL)


# Solution 3: The changes in "Profit/Losses" over the entire period, and then the average of those changes
# setting variable for loop - # averageChange = (totalPnL[1]- totalPnL[0])

x = 1
y = 0

for month in range(totalMonth-1):
    averageChange = (PnL[x]-PnL[y])

# Appending values in List and incrementing loop for both x & y by 1
    changesPnL.append(int(averageChange))
    x+=1
    y+=1

# finding change of P & L and average for the entire period 
avg_change_PnL = round(sum(changesPnL)/ (totalMonth-1),2)
# print("Average Change : " , avg_change_PnL)

# Solution 4: The greatest increase in profits (date and amount) over the entire period
greatestIncrease = max(changesPnL)
maxMonthindex = (monthCount[changesPnL.index(greatestIncrease)+1])
# print ("Greatest increase in Profit : ", maxMonthindex, greatestIncrease)

   
# Solution 5: The greatest decrease in profits (date and amount) over the entire period
greatestDecrease = min(changesPnL) # min of Net total amt
minMonthindex = (monthCount[changesPnL.index(greatestDecrease)+1]) # 
# print ("Greatest Decrease in Profit : ", minMonthindex ,greatestDecrease)   

# print the analysis to the terminal
print("Financial Analysis")
print("----------------------------" )    
print(f"Total Months :  {totalMonth}")
print(f"Total : ${totalPnL}")
print(f"Average Change : ${avg_change_PnL}")
print(f"Greatest increase in Profit : {maxMonthindex} (${greatestIncrease})")
print(f"Greatest Decrease in Profit : {minMonthindex} (${greatestDecrease})")

# creating finacial Analysis text report - Method 1
# Open a file in write mode
with open('PybankAnalysis.txt', 'w') as file:
    # Print to the file
    print("Financial Analysis", file=file)
    print("----------------------------", file=file )    
    print(f"Total Months :  {totalMonth}", file=file)
    print(f"Total : ${totalPnL}", file=file)
    print(f"Average Change : ${avg_change_PnL}", file=file)
    print(f"Greatest increase in Profit : {maxMonthindex} (${greatestIncrease})", file=file)
    print(f"Greatest Decrease in Profit : {minMonthindex} (${greatestDecrease})", file=file)
    
# creating finacial Analysis text report - Method 2
import sys
with open('output.txt', 'w') as file:
    sys.stdout = file
    print("Financial Analysis")
    print("----------------------------" )    
    print(f"Total Months :  {totalMonth}")
    print(f"Total : ${totalPnL}")
    print(f"Average Change : ${avg_change_PnL}")
    print(f"Greatest increase in Profit : {maxMonthindex} (${greatestIncrease})")
    print(f"Greatest Decrease in Profit : {minMonthindex} (${greatestDecrease})")
    sys.stdout = sys.__stdout__  # Reset stdout to the default


"""
INSTRUCTION:-
 In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
 Your task is to create a Python script that analyzes the records to calculate each of the following values:

 '''
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# Your analysis should align with the following results:
'''
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.
"""






















