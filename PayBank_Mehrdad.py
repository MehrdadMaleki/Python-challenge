import pandas as pd 

import sys


#Read the file by using the address of CSV file

file= "../resources/budget_data.csv"

paybank=pd.read_csv(file)

#I have splited the column date to find out the number of months

paybank[["month", "year"]] = paybank["Date"].str.split("-", expand=True)

#The total number of months included in the dataset

total_uniqe_number_month=paybank["month"].nunique()
total_number_month= paybank["month"].count()

#The net total amount of "Profit/Losses" over the entire period

net_total_ProfitLosses=paybank["Profit/Losses"].sum()

#calculation of number of rows for using in the For loop

paybank_index = paybank.index
count_row = len(paybank_index)


#calculation the changes over the entire period

changescollector=[]


for i in range(1,count_row):
    change = paybank.iloc[i,1] - paybank.iloc[i-1,1] 
    changescollector.append(change)
    
#The average of the changes in "Profit/Losses" over the entire period

average_of_the_changes_ProfitLosses= round(sum(changescollector) / len(changescollector),2) 

#The greatest increase in profits (date and amount) over the entire period

maxchange= max(changescollector)
maxindex=changescollector.index(maxchange)
GreatestIncreaseinProfits=paybank.iloc[maxindex+1,0] 

#The greatest decrease in losses (date and amount) over the entire period

minchange= min(changescollector)
minindex=changescollector.index(minchange)
Greatestdecreaseinlooses=paybank.iloc[minindex+1,0] 

print(" -------------------------------- ")
print(" Financial Analysis ")
print(" -------------------------------- ")
print(" total months : " , total_number_month)
print(" total : $",net_total_ProfitLosses)
print(" average changes : $",average_of_the_changes_ProfitLosses)
print(" Greatest Increase in Profits :", GreatestIncreaseinProfits ,"$" , maxchange)
print(" Greatest decrease in Losses :", Greatestdecreaseinlooses ,"$" , minchange)






sys.stdout = open("../resources/PayBank Result.txt" , "w")


print(" -------------------------------- ")
print(" Financial Analysis ")
print(" -------------------------------- ")
print(" total months : " , total_number_month)
print(" total : $",net_total_ProfitLosses)
print(" average changes : $",average_of_the_changes_ProfitLosses)
print(" Greatest Increase in Profits :", GreatestIncreaseinProfits ,"$" , maxchange)
print(" Greatest decrease in Losses :", Greatestdecreaseinlooses ,"$" , minchange)



















