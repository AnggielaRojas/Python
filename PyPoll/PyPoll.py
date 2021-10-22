import os
import csv

PyPoll_csv = os.path.join("..", "Resources", "election_data.csv")

candidates = ['Khan', 'Correy','Li','OTolley'] 
print('Election Results')
print('-------------------')
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    Khan=0
    Correy=0
    Li=0
    OTooley=0
    votes=0
    for row in csvreader:
        votes +=1 
        if row[2]=='Khan':
            Khan +=1
        elif row[2]== 'Correy':
            Correy +=1
        elif row[2]== 'Li':
            Li +=1
        elif row[2]== "O'Tooley":
            OTooley +=1
    print('Total votes: ' + str(votes))

    percentage_Khan = round((Khan/votes*100),2)
    percentage_Correy = round((Correy/votes*100),2)
    percentage_Li = round((Li/votes*100),2)
    percentage_OTooley = round((OTooley/votes*100),2)

    
    print('Khan : ' + str(Khan)+' '+ str(percentage_Khan)+ '%')
    print('Correy : ' + str(Correy)+' '+ str(percentage_Correy)+ '%')
    print('Li : ' + str(Li)+' '+ str(percentage_Li)+'%')
    print("O'Tolley : " + str(OTooley)+' '+ str(percentage_OTooley)+'%')

    print('-------------------')
    if Khan>Correy and Khan>Li and Khan>OTooley:
        print ('Winner: Kahn')
    elif Correy>Khan and Correy>Li and Correy>OTooley:
        print('Winner : Correy')
    elif Li>Khan and Li>Correy and Li>OTooley:
        print('Winner : Li')
    elif OTooley>Khan and OTooley>Correy and OTooley>Li:
        print("Winner : O'Tooley")
    print('-------------------')
  