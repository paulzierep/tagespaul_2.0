from datetime import datetime


# day_of_year = datetime.now().timetuple().tm_yday

files = [0,1,2]

for day_of_year in range(10):

	file_id = day_of_year % len(files)

	print(day_of_year, file_id)