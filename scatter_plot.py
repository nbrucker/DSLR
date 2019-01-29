import sys
import matplotlib.pyplot as plt

import check
import parse
import error

def scale(values):
	i = 0
	min = values['min']
	max = values['max']
	while (i < len(values['notes'])):
		if (values['notes'][i] is not None):
			value = values['notes'][i]
			value = (value - min) / (float(max - min) if float(max - min) != 0 else 1)
			values['notes'][i] = value
		i += 1
	return values

def getValues(data):
	values = {}
	i = 6
	while (i < len(data[0])):
		values[data[0][i]] = {}
		values[data[0][i]]['houses'] = []
		values[data[0][i]]['notes'] = []
		values[data[0][i]]['max'] = None
		values[data[0][i]]['min'] = None
		j = 1
		while (j < len(data)):
			values[data[0][i]]['houses'].append(data[j][1])
			if (check.isFloat(data[j][i])):
				value = float(data[j][i])
				values[data[0][i]]['notes'].append(value)
				if (value > values[data[0][i]]['max'] or values[data[0][i]]['max'] is None):
					values[data[0][i]]['max'] = value
				if (value < values[data[0][i]]['min'] or values[data[0][i]]['min'] is None):
					values[data[0][i]]['min'] = value
			else:
				values[data[0][i]]['notes'].append(None)
			j += 1
		i += 1
	for key in values:
		values[key] = scale(values[key])
	return values

def main():
	if (len(sys.argv) != 2):
		error.error('python scatter_plot.py [file]')
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
	i = 0
	x = 15
	while (i < len(names)):
		j = i + 1
		while (j < len(names)):
			if (x >= 15):
				plt.figure(i, figsize=(25, 15))
				x = 0
			plt.subplot(3, 5, x + 1)
			n = 0
			a = []
			b = []
			c = []
			while (n < len(values[names[i]]['notes'])):
				if (values[names[i]]['notes'][n] is not None and values[names[j]]['notes'][n] is not None):
					a.append(values[names[i]]['notes'][n])
					b.append(values[names[j]]['notes'][n])
					if (values[names[i]]['houses'][n] == 'Slytherin'):
						c.append('green')
					elif (values[names[i]]['houses'][n] == 'Hufflepuff'):
						c.append('yellow')
					elif (values[names[i]]['houses'][n] == 'Ravenclaw'):
						c.append('blue')
					else:
						c.append('red')
				n += 1
			plt.scatter(a, b, color=c, alpha=0.6)
			plt.title(names[i] + ' vs ' + names[j], fontsize=15)
			j += 1
			x += 1
		i += 1
	plt.show()

if __name__ == '__main__':
	main()
