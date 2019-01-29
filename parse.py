def parseCSV(content):
	content = content.split('\n')
	i = 0
	data = []
	x = -1
	while (i < len(content)):
		tmp = content[i].split(',')
		if (len(tmp) == x or x == -1):
			data.append(tmp)
			x = len(tmp)
		i += 1
	return data
