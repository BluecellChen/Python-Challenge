#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Import Modules / Dependencies
import os
import csv
# Create file path
csv_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")


# In[31]:


# Read in the CSV file
with open(csv_path, newline="") as csvfile:
    # Split the data on commas   
    csv_reader = csv.reader(csvfile, delimiter = ',')
    header = next(csv_reader)
    #create variables / lists to add the csv values to 
    month = []
    #total_profit = 0
    profit = []
    change_profit = []
        # Loop through the data
    for row in csv_reader:
        #total_month = total_month + 1
        #total_profit = total_profit + (int(row[1]))
        month.append(row[0])
        profit.append(int(row[1]))
        Total_Month = len(month)
        
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])

#The greatest increase in profits                     
increase = max(change_profit)
#The greatest decrease in losses
decrease = min(change_profit)

month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


# In[38]:


output = os.path.join("..", "PyBank", "Resources", "PyBankOutput.txt")
with open(output,"w") as PyBank_analysis:
    PyBank_analysis.write(f"Financial Analysis\n")
    PyBank_analysis.write("----------------------------\n")
    PyBank_analysis.write(f"Total Months:{len(month)}\n")    
    PyBank_analysis.write(f"Total: ${sum(profit)}\n")    
    PyBank_analysis.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}\n")
    PyBank_analysis.write(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})\n")
    PyBank_analysis.write(f"Greatest Decrease in Profits: {month[month_decrease]} (${(str(decrease))})\n")
    
    with open(output, 'r') as readfile:
        print(readfile.read())


# In[42]:


print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {len(month)}")
print(f"Total: {sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month[month_decrease]} (${(str(decrease))})")


# In[ ]:




