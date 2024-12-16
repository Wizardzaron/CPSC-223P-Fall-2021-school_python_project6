from weather import *
import calendar
weather = {}
f = ''
choice = 0
while(choice >= 0 and choice < 5):
	print("                  *** Tuffy Titan Weather Logger Main Menu")
	print("1.)Set data filename   ")
	print("2.)Add weather data")
	print("3.)Print daily report")
	print("4.)Print historical report")
	print("5.)Exit the program")
	choice = int(input("Enter menu choice:"))
	if choice == 1:
		f = input("Enter the filename:")
		weather = read_data(filename = f)
	elif choice == 2:
		date = int(input("Enter date (YYYYMMDD):"))
		ti = int(input("Enter time (hhmmss):"))
		te = int(input("Enter temperature:"))
		hu = int(input("Enter humidity:"))
		ra = int(input("Enter rainfall:"))
		date = str(date)
		ti = str(ti)
		data ={date+ti: {'t':te, 'h':hu, 'r':ra}} 
		write_data(data = data, filename = 'filename')
	elif choice == 3:
		date = input("Enter the date of the day you want to report, do it in YYYYMMDD")
		date_conversion = calendar.month_name[int(date[4:6])]
		day = int(date[6:8])
		print("====================================Daily Report=============================================")
		print("Date             Time               Temperature         Humidity            Rainfall")
		print(f'{date_conversion:7}{day:2d},{date[0:4]:10}{date[2:4]}{date[4:6]:4}{te:13}           {hu:10}        {ra}')
	elif choice == 4:
		print("====================================Historical Report========================================")
		print("Date                       Max Temp    Min Temp        Max Humid      Min Humid           Rainfall")
		data = read_data(filename = f)
		date_conversion = calendar.month_name[int(date[4:6])]
		day = int(date[6:8])
		min_temp = min_temperature(data = data, date = date)
		max_temp = max_temperature(data = data, date = date)
		min_humid = min_humidity(data = data, date = date)
		max_humid = max_humidity(data = data, date = date)
		total_rain = tot_rain(data = data, date = date)
		print(f'{date_conversion:7}{day:2d}, {date[0:4]:7}{min_temp:5} {max_temp:5}{min_humid:10} {max_humid:5} {total_rain}')
