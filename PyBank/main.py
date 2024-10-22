import csv
import os

from pathlib import Path

budget_data = Path(__file__).parent / "Resources" / "budget_data.csv" # Input file path
file_to_output = Path(__file__).parent /"analysis"/"budget_analysis.txt" # Output file path
totalMonths=0
totalprofit=0

# Add more variables to track other necessary financial data

profitDeltas=[]
currentDelta=0
profits=[]
DeltaSum=0
AverageChange=0
MaxValue=0
MinValue=0
Dates=[]

#Open file
with open(budget_data) as PayBankCsv: #Open file
    PayBankReader = csv.reader(PayBankCsv) #read file
    header = next(PayBankReader) #skip and Save the header #"["Date","234343"]" 

    for row in PayBankReader: #Row gives back each row in a list form ["Date","234343"]
        totalMonths=totalMonths+1
        totalprofit=totalprofit+int(row[1]) 
        profits.append(int(row[1])) #Create a list of all values in column Profit/Loss
        Dates.append(row[0])
    

for i in range(len(profits)): #Loop through which the Profits Deltas will be calculated 
    if i < (len(profits)-1):
        currentDelta=profits[i+1]-profits[i]
        profitDeltas.append(int(currentDelta)) #Create a list to store the Profit Deltas
    
for i in range(len(profitDeltas)): #Loop through which we will sum all the Profit Deltas
    DeltaSum=DeltaSum+profitDeltas[i]

for i in range(len(profitDeltas)-1): #Calculate de greatest increase(max) and the greatest decrease(min)
    if int(profitDeltas[i]) > MaxValue:
        MaxValue=int(profitDeltas[i])

    elif int(profitDeltas[i]) < MinValue:
        MinValue=int(profitDeltas[i])

AverageChange=DeltaSum/(len(profitDeltas))


#Resultados

print("Financial Analysis")
print("------------------------")    
print(f"Total Months: {totalMonths}")
print(f"Total Profit: {totalprofit}")
print(f"Average Change: {AverageChange}")
print(f"Greatest Increase in Profits: {Dates[(profitDeltas.index(MaxValue))+1]} {MaxValue}")
print(f"Greatest Decease in Profits: {Dates[(profitDeltas.index(MinValue))+1]} {MinValue}")

with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis \n")
    txt_file.write("------------------------ \n")
    txt_file.write(f"Total Months: {totalMonths} \n")
    txt_file.write(f"Total Profit: {totalprofit} \n")
    txt_file.write(f"Average Change: {AverageChange} \n")
    txt_file.write(f"Greatest Increase in Profits: {Dates[(profitDeltas.index(MaxValue))+1]} {MaxValue} \n")
    txt_file.write(f"Greatest Decease in Profits: {Dates[(profitDeltas.index(MinValue))+1]} {MinValue} \n")

