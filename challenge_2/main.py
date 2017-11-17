import os
import numpy as np
import csv

csvpath1 = os.path.join('PyPoll/raw_data', 'election_data_2.csv')

#csvpath2 = os.path.join('PyPoll/raw_data', 'election_data_2.csv')


total_vote =  0
candidate = {'candidate name': [],
			'votes': {}
			}



with open(csvpath1, newline ="") as csvfile1:

	csvreader1 = csv.reader(csvfile1, delimiter = ",")

	for row in csvreader1:

		if row[0].lower() == 'voter id':

			continue

		if row[2] not in candidate['votes'].keys():

				candidate['candidate name'].append(row[2])
				candidate['votes'][row[2]] = 1

				total_vote = total_vote + 1

		elif row[2] in candidate['votes'].keys():

				candidate['votes'][row[2]] = candidate['votes'][row[2]] + 1

				total_vote = total_vote + 1

print("Election Results")
print('---------------------------------------')
print("Total Votes were " + str(total_vote))
print('---------------------------------------')

for key,value in candidate['votes'].items():

	print('Candidate ' + key + ' had ' + str(value) + ' - ' + str(round((int(value)/int(total_vote))*100)) + '% of the total vote.')

max_value = max(candidate['votes'].values())
max_keys = str([k for k, v in candidate['votes'].items() if v == max_value])[1:-1].replace("'",'')
	
print('Winner is ' + str(max_keys) + ' with ' + str(max_value) + ' votes!')



output_csvpath = os.path.join('output',"challenge2.csv")

with open(output_csvpath, 'w', newline = "") as csvfile:

	csvwriter = csv.writer(csvfile, delimiter = ",")

	csvwriter.writerow(['Candidate','Votes','Percentage of votes','Winner'])
	
	for candidatex,value in candidate['votes'].items():

		if candidatex == max_keys:

			csvwriter.writerow([candidatex,value,round(value/total_vote*100),'XX'])

		else:
			
			csvwriter.writerow([candidatex,value,round(value/total_vote*100)])

	csvwriter.writerow(['Total Votes',total_vote,round(total_vote/total_vote*100)])

	