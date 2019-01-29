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
	data = data.drop(columns=['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
	sns.pairplot(data)


if __name__ == '__main__':
	main()
