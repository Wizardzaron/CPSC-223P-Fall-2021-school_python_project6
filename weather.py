import json
def read_data(*, filename):
	t = {}
	try:
		with  open(filename, 'r') as b:
			w = json.load(b)
			return w
	except FileNotFoundError:
		return t

def write_data(data, filename):
	t = {}
	z = open(filename, 'w')
	t = json.dump(data,z)
	return t
def max_temperature(*, data, date):
	max_temp = 0
	for y,z in data.items():
		if date in y:
			x = data[y]['t']
			if max_temp < x:
				max_temp = x
	return max_temp

def min_temperature(*, data, date):
	min_temp = 100
	for y,z in data.items():
		if date in y:
			x = data[y]['t']
			if min_temp > x:
				min_temp = x
	return min_temp

def max_humidity(data, date):
	max_humid = 0
	for y,z in data.items():
		if date in y:
			x = data[y]['h']
			if max_humid < x:
				max_humid = x
	return max_humid

def min_humidity(data, date):
	min_humid = 100
	for y,z in data.items():
		if date in y:
			x = data[y]['h']
			if min_humid > x:
				min_humid = x
	return min_humid

def tot_rain(data, date):
	total_rain = 0
	for y,z in data.items():
		if date in y:
			x = data[y]['r']
			total_rain = total_rain + x
	return total_rain
