import sys
import pandas
import math
import json

import error
from logreg_train import sigmoid

important = ['Astronomy', 'Herbology', 'Divination', 'Muggle Studies', 'History of Magic', 'Transfiguration', 'Charms', 'Flying']

def main():
	if (len(sys.argv) != 3):
		error.error('python logreg_predict.py [file] [file]')
	filename = sys.argv[1]
	thetas = sys.argv[2]
	data = []
	try:
		data = pandas.read_csv(filename)
		f = open(thetas, 'r')
		thetas = f.read()
		f.close()
	except:
		error.error('error opening file')
	thetas = json.loads(thetas)
	droping = []
	for x in data:
		if (x not in important):
			droping.append(x)
	data = data.drop(columns=droping)
	results = data.max() - data.min()
	for i in range(len(results)):
		if (results[i] == 0):
			results[i] = 1
	data = (data - data.min()) / results
	output = 'Index,Hogwarts House\n'
	for index, row in data.iterrows():
		grades = row.tolist()
		h_max = None
		v_max = None
		for house in thetas:
			theta = thetas[house]
			x = theta[0]
			for i in range(len(grades)):
				if (math.isnan(grades[i])):
					continue
				x += grades[i] * theta[i + 1]
			x = sigmoid(x)
			if (v_max is None or x > v_max):
				v_max = x
				h_max = house
		output += str(index) + ',' + h_max + '\n'
	open('houses.csv', 'w').close()
	f = open('houses.csv', 'w')
	f.write(output)
	f.close()

if __name__ == '__main__':
	main()
