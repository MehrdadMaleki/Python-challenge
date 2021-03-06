import pandas as pd

#Read the file by using the address of CSV file

file= "../Resources/election_data.csv"

paypoll=pd.read_csv(file)

#The total number of votes cast

TotalVotes= paypoll["Voter ID"].count()

#A complete list of candidates who received votes

listofcandidates= paypoll["Candidate"].unique()

#The list of total number of votes each candidate won

numbervotes=[]

for x in listofcandidates:
    number1=(paypoll["Candidate"] == x).sum()
    numbervotes.append(number1)

Winner=max(numbervotes)


print(" -------------------------------- ")
print(" Election Results ")
print(" -------------------------------- ")

print("Total Votes :",TotalVotes)

print(" -------------------------------- ")

#The percentage of votes each candidate won

for x in listofcandidates:
    number=(paypoll["Candidate"] == x).sum()
    percentage=round((number/TotalVotes)*100,3)
    print( x , percentage,"%"," (",number,")") 


print(" -------------------------------- ")

#The winner of the election based on popular vote

for x in listofcandidates:
    numberwin=(paypoll["Candidate"] == x).sum()
    if numberwin == Winner:
        print("Winner : " , x)
    else:
        pass

print(" -------------------------------- ")































