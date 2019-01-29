import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import parse
import error
import check

houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']

def scale(values):
	j = 0
	min = values['min']
	max = values['max']
	while (j < len(houses)):
		i = 0
		while (i < len(values[houses[j]])):
			value = values[houses[j]][i]
			value = (value - min) / (float(max - min) if float(max - min) != 0 else 1)
			values[houses[j]][i] = value
			i += 1
		j += 1
	return values

def getValues(data):
	values = {}
	i = 6
	while (i < len(data[0])):
		values[data[0][i]] = {}
		values[data[0][i]]['Gryffindor'] = []
		values[data[0][i]]['Ravenclaw'] = []
		values[data[0][i]]['Hufflepuff'] = []
		values[data[0][i]]['Slytherin'] = []
		values[data[0][i]]['max'] = None
		values[data[0][i]]['min'] = None
		j = 1
		while (j < len(data)):
			if (data[j][1] in values[data[0][i]] and check.isFloat(data[j][i])):
				value = float(data[j][i])
				values[data[0][i]][data[j][1]].append(value)
				if (value > values[data[0][i]]['max'] or values[data[0][i]]['max'] is None):
					values[data[0][i]]['max'] = value
				if (value < values[data[0][i]]['min'] or values[data[0][i]]['min'] is None):
					values[data[0][i]]['min'] = value
			j += 1
		i += 1
	for key in values:
		values[key] = scale(values[key])
	return values

def main():
	if (len(sys.argv) != 2):
		error.error('python histogram.py [file]')
	filename = sys.argv[1]
	content = ''
	try:
		f = open(filename, 'r')
		content = f.read()
		f.close()
	except:
		error.error('error opening file')
	data = parse.parseCSV(content)
	names = data[0][6:]
	values = getValues(data)
	plt.figure(figsize=(25, 15))
	i = 0
	while (i < len(names)):
		plt.subplot(3, 5, i + 1)
		plt.hist(values[names[i]]['Gryffindor'], color='red', alpha=0.6)
		plt.hist(values[names[i]]['Hufflepuff'], color='yellow', alpha=0.6)
		plt.hist(values[names[i]]['Slytherin'], color='green', alpha=0.6)
		plt.hist(values[names[i]]['Ravenclaw'], color='blue', alpha=0.6)
		plt.title(names[i], fontsize=15)
		i += 1
	plt.subplot(3, 5, i + 1)
	handles = [Rectangle((0, 0), 1, 1, color=c, ec="k", alpha=0.6) for c in ['red', 'yellow', 'green', 'blue']]
	labels = ["Gryffindor", "Hufflepuff", "Slytherin", 'Ravenclaw']
	plt.legend(handles, labels)
	plt.title("Legend", fontsize=15)
	plt.xlabel('grades')
	plt.ylabel('number of students')
	plt.show()

if __name__ == '__main__':
	main()
