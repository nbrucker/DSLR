import sys
import pandas
import math
import json

import error

important = ['Astronomy', 'Herbology', 'Divination', 'Muggle Studies', 'History of Magic', 'Transfiguration', 'Charms', 'Flying']

houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']

output = {}

def sigmoid(x):
	return (1 / (1 + math.exp(-x)))

def hypothesis(grades, thetas):
	x = thetas[0]
	for i in range(len(grades)):
		x += grades[i] * thetas[i + 1]
	return (sigmoid(x))

def reg(data, house, students_house):
	thetas = [0] * (len(data.columns) + 1)
	m = len(data)
	old_cost = None
	cost = None
	i = 0
	lr = 1 / float(m)
	while (old_cost is None or round(old_cost, 6) != round(cost, 6)):
		old_cost = cost
		cost = 0
		modif_thetas = [0] * (len(data.columns) + 1)
		for index, row in data.iterrows():
			grades = row.tolist()
			x = hypothesis(grades, thetas)
			y = 1 if house == students_house[index] else 0
			cost += -y * math.log(x) + (1 - y) * math.log(1 - x)
			for n in range(len(modif_thetas)):
				grade = 1
				if (n > 0):
					grade = grades[n - 1]
				modif_thetas[n] += (x - y) * grade
		cost *= (1 / float(m))
		for n in range(len(thetas)):
			thetas[n] -= modif_thetas[n] * lr
		i += 1
	output[house] = thetas

def main():
	if (len(sys.argv) != 2):
		error.error('python logreg_train.py [file]')
	filename = sys.argv[1]
	data = []
	try:
		data = pandas.read_csv(filename)
	except:
		error.error('error opening file')
	data = data.dropna()
	students_house = data['Hogwarts House']
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
	for house in houses:
		print(house)
		reg(data, house, students_house)
	open('thetas.json', 'w').close()
	f = open('thetas.json', 'w')
	f.write(json.dumps(output))
	f.close()

if __name__ == '__main__':
	main()
