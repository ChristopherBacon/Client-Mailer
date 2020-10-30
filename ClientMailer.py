

'''
1. Get Client Data
2. create class / database not sure as yet
3. test send email
4. create library of email messages
5. create scheduler to determine mailsend.

'''

import pandas as pd
import csv


def main():
	get_clients2()
	print('test first')

#filepath = [r'/Users/christopherbacon/Downloads/jstdatasetr4.csv']
#def get_clients():
	#with open(filepath) as f:
		#rows = f.reader(csv, delimiter=',')
		#data = []
		#for row in rows:
			#data.append(row)
filepath = '/Users/christopherbacon/Downloads/jstdatasetr4.csv'
def get_clients2():
	df = pd.read_csv(filepath)
	print(df)


















if __name__ == "__main__":
	main()

