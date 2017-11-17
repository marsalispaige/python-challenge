import os
import numpy as np
import csv

csvpath1 = os.path.join('PyBank/raw_data', 'budget_data_1.csv')

csvpath2 = os.path.join('PyBank/raw_data', 'budget_data_2.csv')


total_months =  0
total_revenue = 0
revenue_chng = []
revenue_date = []
revenue_prev = 0




with open(csvpath1, newline ="") as csvfile1:

	csvreader1 = csv.reader(csvfile1, delimiter = ",")

	for row in csvreader1:

		if row[0].lower() == 'date':

			continue


		total_months = total_months + 1
		total_revenue = total_revenue + int(row[1])
		revenue_date.append(row[0])
		revenue_chng.append(int(row[1])-int(revenue_prev))
		revenue_prev = row[1]


revenue_prev = 0

with open(csvpath2, newline ="") as csvfile2:

	csvreader2 = csv.reader(csvfile2, delimiter = ",")

	for row in csvreader2:

		if row[0].lower() == 'date':

			continue

		total_months = total_months + 1
		total_revenue = total_revenue + int(row[1])
		revenue_date.append(row[0])
		revenue_chng.append(int(row[1])- int(revenue_prev))
		revenue_prev = row[1]


revenue_chng_avg = np.mean(revenue_chng)


print("Financial Analyst")
print('Total number of months is ' + str(total_months))
print('Total amount of revenue accrued is ' + str(total_revenue))
print('The average change in revenue is ' + str(np.mean(revenue_chng)))

for a,b in zip(revenue_date,revenue_chng):

	if b == max(revenue_chng):

		print('Greatest increase in revenue: ' + str(a) + ' (' + str(b) + ')')

		revenue_inc_date = a
		revenue_inc = b 

	elif b == min(revenue_chng):

		print('Greatest Decrease in revenue: ' + str(a) + ' (' + str(b) +')')

		revenue_dec_date = a
		revenue_dec = b 


output_csvpath = os.path.join('output',"challenge1.csv")

with open(output_csvpath, 'w', newline = "") as csvfile:

	csvwriter = csv.writer(csvfile, delimiter = ",")

	csvwriter.writerow(['Total Months','Total Revenue','Greatest Increase in Revenue','Date','Greatest Decrease in Revenue','Date','Average Change in Revenue'])

	csvwriter.writerow([total_months, total_revenue, revenue_inc, revenue_inc_date, revenue_dec, revenue_dec_date, revenue_chng_avg])


