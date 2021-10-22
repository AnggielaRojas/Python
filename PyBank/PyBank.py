import os
import csv

PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")

print('Financial Analysis')
print('-----------------------')

total=[]
months=[]
monthly_change=[]

with open(PyBank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  

    for row in csvreader:
        months.append(row[0])
        total.append(int(row[1]))

    revenue=0
    for values in total:
        revenue += int(values)
    print("Total :  " ,revenue)
    print("Total months: ", len(months))

    for i in range(len(total)-1):
        monthly_change.append(total[i+1]-total[i])

max_increase= max(monthly_change)
min_decrease= min(monthly_change)
max_month= monthly_change.index(max(monthly_change))+1
min_month= monthly_change.index(min(monthly_change))+1
print('Greatest Increase in Profits: '+ months[max_month]+' '+ (str(max_increase)))
print('Greatest Decrease in Profits: '+ months[min_month]+' '+ (str(min_decrease)))
print('Average Change:'+ str(round(sum(monthly_change)/len(monthly_change),2)))
