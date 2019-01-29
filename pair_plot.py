import sys

import seaborn as sns
import error
from histogram import getValues
import parse

def main():
	if (len(sys.argv) != 2):
		error.error('python pair_plot.py [file]')
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
				# plt.figure(i, figsize=(25, 15))
				x = 0
			# plt.subplot(3, 5, x + 1)
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
			sns.pairplot(a)
			# plt.scatter(a, b, color=c, alpha=0.6)
			# plt.title(names[i] + ' vs ' + names[j], fontsize=15)
			j += 1
			x += 1
		i += 1

if __name__ == '__main__':
		main()