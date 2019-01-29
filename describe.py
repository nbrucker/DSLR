import sys
import math

import error
import parse
import check

def getEcarts(data, n):
	valid = []
	i = 1
	while (i < len(data)):
		if (check.isFloat(data[i][n])):
			valid.append(float(data[i][n]))
		i += 1
	i = 0
	while (i < len(valid)):
		j = i + 1
		while (j < len(valid)):
			if (valid[j] < valid[i]):
				tmp = valid[j]
				valid[j] = valid[i]
				valid[i] = tmp
			j += 1
		i += 1
	first = int(math.ceil(len(valid) / 4))
	second = int(math.ceil(len(valid) / 2))
	third = int(len(valid) - first)
	return valid[first], valid[second], valid[third]

def getMin(data, n):
	x = None
	i = 1
	while (i < len(data)):
		if (check.isFloat(data[i][n]) and (x > float(data[i][n]) or x is None)):
			x = float(data[i][n])
		i += 1
	return x

def getMax(data, n):
	x = None
	i = 1
	while (i < len(data)):
		if (check.isFloat(data[i][n]) and (x < float(data[i][n]) or x is None)):
			x = float(data[i][n])
		i += 1
	return x


def getCount(data, n):
	x = 0
	i = 1
	while (i < len(data)):
		if (check.isFloat(data[i][n])):
			x += 1
		i += 1
	return x

def getSomme(data, n):
	x = 0
	i = 1
	while (i < len(data)):
		if (check.isFloat(data[i][n])):
			x += float(data[i][n])
		i += 1
	return x

def getStd(data, n, mean):
	x = 0
	j = 0
	i = 1
	while (i < len(data)):
		if (check.isFloat(data[i][n])):
			x += math.pow(float(data[i][n]) - mean, 2)
			j += 1
		i += 1
	x /= j
	return math.sqrt(x)

def feature(data):
	features = {}
	i = 6
	while (i < len(data[0])):
		features[data[0][i]] = {}
		features[data[0][i]]["Count"] = getCount(data, i)
		features[data[0][i]]["Mean"] = getSomme(data, i) / features[data[0][i]]["Count"]
		features[data[0][i]]["Std"] = getStd(data, i, features[data[0][i]]["Mean"])
		features[data[0][i]]["Min"] = getMin(data, i)
		features[data[0][i]]["25%"], features[data[0][i]]["50%"], features[data[0][i]]["75%"] = getEcarts(data, i)
		features[data[0][i]]["Max"] = getMax(data, i)
		i += 1
	return features

def printData(features, name, names):
	s = name
	j = 0
	while (len(name) + j != 5):
		s += " "
		j += 1
	i = 0
	while (i < len(names)):
		j = 0
		while (features[names[i]]["size"] - len(str(features[names[i]][name])) + 5 - j != 0):
			s += ' '
			j += 1
		s += str(features[names[i]][name])
		i += 1
	print(s)

def main():
	if (len(sys.argv) != 2):
		error.error('python describe.py [file]')
	filename = sys.argv[1]
	content = ''
	try:
		f = open(filename, 'r')
		content = f.read()
		f.close()
	except:
		error.error('error opening file')
	data = parse.parseCSV(content)
	features = feature(data)
	for key in features:
		max = len(key)
		for el in features[key]:
			features[key][el] = '{:.6f}'.format(round(features[key][el], 6))
			if (len(str(features[key][el])) > max):
				max = len(str(features[key][el]))
		features[key]['size'] = max
	s = "     "
	i = 6
	while (i < len(data[0])):
		j = 0
		while (features[data[0][i]]["size"] - len(data[0][i]) + 5 - j != 0):
			s += " "
			j += 1
		s += data[0][i]
		i += 1
	print(s)
	printData(features, "Count", data[0][6:])
	printData(features, "Mean", data[0][6:])
	printData(features, "Std", data[0][6:])
	printData(features, "Min", data[0][6:])
	printData(features, "25%", data[0][6:])
	printData(features, "50%", data[0][6:])
	printData(features, "75%", data[0][6:])
	printData(features, "Max", data[0][6:])


if __name__ == '__main__':
	main()
