
# please read code from visiting each folder Path individually`./python-challenge/Starter_Code/PyBank/Resources`

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
    
# # solution 1: 
# Looping for Total number of month & Net total profit & loss

    for row in csv_reader :
        monthCount.append(row[0])
        PnL.append(int(row[1]))

# total number of month count
    totalMonth = len(monthCount)
    
# Solution 2 : The net total amount of "Profit/Losses" over the entire period
    totalPnL = sum(PnL)
    

# Solution 3: The changes in "Profit/Losses" over the entire period, and then the average of those changes
# setting variable for loop - # averageChange = (totalPnL[1]- totalPnL[0])

x = 1
y = 0

for month in range(totalMonth-1): # -1 upto the last range index
    averageChange = (PnL[x]-PnL[y])

# Appending values in List and incrementing loop for both x & y by 1
    changesPnL.append(int(averageChange))
    x+=1
    y+=1

# finding change of P & L and average for the entire period 
avg_change_PnL = round(sum(changesPnL)/ (totalMonth-1),2)

# Solution 4: The greatest increase in profits (date and amount) over the entire period
greatestIncrease = max(changesPnL)
maxMonthindex = (monthCount[changesPnL.index(greatestIncrease)+1])

   
# Solution 5: The greatest decrease in profits (date and amount) over the entire period
greatestDecrease = min(changesPnL) # min of Net total amt
minMonthindex = (monthCount[changesPnL.index(greatestDecrease)+1]) # 

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
    
