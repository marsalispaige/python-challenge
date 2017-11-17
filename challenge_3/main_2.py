import os
import numpy as np
import csv

csvpath1 = os.path.join('PyBoss/raw_data', 'employee_data1.csv')

csvpath2 = os.path.join('PyBoss/raw_data', 'employee_data2.csv')



emid = []
first_name = []
last_name = []
dob = []
ssn = []
state = []
			

def stateabv(state):

	csvpath3 = os.path.join('resources/statesabv.csv')

	with open(csvpath3, newline ="") as csvstate:

		csvreader_state = csv.reader(csvstate, delimiter = ",")

		for row in csvreader_state:

			if row[0] == state:

				return row[1]





with open(csvpath1, newline ="") as csvfile1:

	csvreader1 = csv.reader(csvfile1, delimiter = ",")

	for row in csvreader1:

		if row[0].lower() == 'emp id':

			continue

		else:

			emid.append(row[0])
			first_name.append(row[1].split()[0])
			last_name.append(row[1].split()[-1])
			dob.append(row[2])
			ssn.append(str('***-**-' + row[3].split('-')[-1]))
			state.append(stateabv(row[4]))


with open(csvpath2, newline ="") as csvfile2:

	csvreader2 = csv.reader(csvfile2, delimiter = ",")

	for row in csvreader2:

		if row[0].lower() == 'emp id':

			continue

		else:

			emid.append(row[0])
			first_name.append(row[1].split()[0])
			last_name.append(row[1].split()[-1])
			dob.append(row[2])
			ssn.append(str('***-**-' + row[3].split('-')[-1]))
			state.append(stateabv(row[4]))



	
employee_file = zip(emid,first_name,last_name,dob,ssn,state)

output_csvpath = os.path.join('output',"challenge3.csv")

with open(output_csvpath, 'w', newline = "") as csvfile:

	csvwriter = csv.writer(csvfile, delimiter = ",")

	csvwriter.writerow(['emid','First name','Last name','DOB','SSN','State'])
	
	for x in employee_file:

			
		csvwriter.writerow(x)


	