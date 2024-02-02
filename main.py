#Modules to import
import os
import csv


#File to Load
csvpath = os.path.join("Resources", "budget_data.csv")
analysis_output = os.path.join("Analysis", "budget_output.txt")
total_months = 0 
#change in months variable 
change_in_months = []
greatest_increase = ['', 0]
greatest_decrease = ['', 10000000]
total_change = []
total_amount = 0 


with open(csvpath) as data:
    csvreader = csv.reader(data)
    header = next(csvreader)
    
    first_row = next(csvreader)
    total_months = total_months + 1 
    total_amount = total_amount + int(first_row[1])
    previous_amount =  int(first_row[1])
    
    for row in csvreader:
        
        
    
    