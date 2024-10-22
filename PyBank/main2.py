import os
import csv

from pathlib import Path

#budget_data = os.path.join("..","OneDrive","Documentos","Data Analytics Bootcamp","Github","python-challenge","PyBank","Resources", "budget_data.csv")  # Input file path
budget_data = Path(__file__).parent /"budget_data.csv" # Input file path
file_to_output = os.path.join("..","Data Analytics Bootcamp","Github","python-challenge","PyBank","analysis","budget_analysis.txt")  # Output file path

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
with open(budget_data) as PayBankCsv:
    PayBankReader = csv.reader(PayBankCsv)
    header= next(PayBankReader)

