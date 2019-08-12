#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import Modules / Dependencies
import os
import csv
# Create file path

csv_path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")
csv_path
#Voter ID,County,Candidate


# In[13]:


# Read in the CSV file
with open(csv_path, newline="") as csvfile:
    # split the data on commas
    csv_reader = csv.reader(csvfile, delimiter = ",")
    header = next(csv_reader)
    # create variables /lists to add the csv values to
    vote_count = 0
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    OTooley_count = 0
    # candidate = []
    # Loop through the data, count the total number of votes
    for row in csv_reader:
        vote_count += 1
        # Calculate total number of votes for each candidate
        if (row[2] == "Khan"):
            Khan_count += 1
        elif (row[2] == "Correy"):
            Correy_count += 1
        elif (row[2] == "Li"):
            Li_count += 1
        else:
            OTooley_count += 1
    # percentage of votes for each candidate
    Khan_percent = Khan_count / vote_count
    Correy_percent = Correy_count / vote_count
    Li_percent = Li_count / vote_count
    OTooley_percent = OTooley_count / vote_count
    # winner has the most votes
    winner = max(Khan_count, Correy_count, Li_count, OTooley_count)

    if winner == Khan_count:
        winner_is = "Khan"
    elif winner == Correy_count:
        winner_is = "Correy"
    elif winner == Li_count:
        winner_is = "Li"
    else:
        winner_is = "O'Tooley" 


# In[15]:


output = os.path.join("..", "PyPoll", "Resources", "PyPollOutput.txt")
with open(output,"w") as PyPoll_analysis:
    PyPoll_analysis.write(f"Election Results\n")
    PyPoll_analysis.write(f"-------------------------\n")
    PyPoll_analysis.write(f"Total Votes: {vote_count}\n")    
    PyPoll_analysis.write(f"-------------------------\n")    
    PyPoll_analysis.write(f"Khan: {Khan_percent:.3%}({Khan_count})\n")
    PyPoll_analysis.write(f"Correy: {Correy_percent:.3%}({Correy_count})\n")
    PyPoll_analysis.write(f"Li: {Li_percent:.3%}({Li_count})\n")
    PyPoll_analysis.write(f"O'Tooley: {OTooley_percent:.3%}({OTooley_count})\n")
    PyPoll_analysis.write(f"-------------------------\n")  
    PyPoll_analysis.write(f"Winner: {winner_is}\n")
    PyPoll_analysis.write(f"-------------------------\n")      
    
with open(output, 'r') as readfile:
    print(readfile.read())


# In[26]:


print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes:{vote_count}")    
print(f"-------------------------")    
print(f"Khan: {Khan_percent:.3%}({Khan_count})")
print(f"Correy: {Correy_percent:.3%}({Correy_count})")
print(f"Li: {Li_percent:.3%}({Li_count})")
print(f"O'Tooley: {OTooley_percent:.3%}({OTooley_count})")
print(f"-------------------------")  
print(f"Winner: {winner_is}")
print(f"-------------------------")  

