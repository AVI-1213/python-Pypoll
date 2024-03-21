# importing modules OS and CSV
import os
import csv

# Declaring CSV file path location 
filepath = os.path.join("..", "Resources", "election_data.csv")

# initializing variable 
totalVote = 0
candidateDict = {}

# reading CSV file using csv.reader from declared file path. 
with open(filepath) as file:
    csvfile = csv.reader(file, delimiter=",")
    next(csvfile)  # Skip header row
    
    # looping in declaring Candidate for last column 2 and incrementing vote by 1 to get total count of Vote cast
    for row in csvfile:
        candidate = row[2]
        totalVote += 1
        
        # storing and incrementing each candidate value using if, else condition 
        if candidate in candidateDict:
            candidateDict[candidate] += 1
        else:
            candidateDict[candidate] = 1

# Print Election Results to Code Terminal

print("Election Results")
print("===========================")
print(f"Total Vote : {totalVote}")
print("===========================")

# calculating percentage of vote by each candidate and printing to terminal
for candidate, votes in candidateDict.items():
    percentVote = (votes / totalVote) * 100
    print(f"{candidate}: {percentVote:.3f}% ({votes})")

print("===========================")

# fetching maximum vote count from candidate dictionary and printing to terminal
winner = max(candidateDict, key=candidateDict.get)
print(f"Winner: {winner}")
print("===========================")

# Write Election Results to a text file
with open('ElectionResults.txt', 'w') as file:
    # Writing Election Results to file
    
    file.write("Election Results\n")
    file.write("===========================\n")
    file.write(f"Total Vote : {totalVote}\n")
    file.write("===========================\n")
    
    # calculating percentage of vote by each candidate and writing to file
    for candidate, votes in candidateDict.items():
        percentVote = (votes / totalVote) * 100
        file.write(f"{candidate}: {percentVote:.3f}% ({votes})\n")
    
    file.write("===========================\n")
    
    # fetching maximum vote count from candidate dictionary and writing to file
    file.write(f"Winner: {winner}\n")
    file.write("===========================\n")
