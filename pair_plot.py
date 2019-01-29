import sys
import seaborn as sns
import pandas

import error

def main():
	if (len(sys.argv) != 2):
		error.error('python pair_plot.py [file]')
	filename = sys.argv[1]
	data = []
	try:
		data = pandas.read_csv(filename)
	except:
		error.error('error opening file')
	data = data.dropna()
	houses = data['Hogwarts House']
	data = data.drop(columns=['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
	results = data.max() - data.min()
	i = 0
	while (i < len(results)):
		if (results[i] == 0):
			results[i] = 1
		i += 1
	data = (data - data.min()) / results
	data['Houses'] = houses
	color = {
		'Gryffindor': 'red',
		'Slytherin': 'green',
		'Ravenclaw': 'blue',
		'Hufflepuff': '#EBEB11'
	}
	options = {
		'alpha': 0.6
	}
	plot = sns.pairplot(data, hue='Houses', palette=color, plot_kws=options)
	plot.savefig("./pair_plot.png")

if __name__ == '__main__':
	main()
