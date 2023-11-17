import random
import os
from datetime import datetime

random.seed(42)


day_of_year = datetime.now().timetuple().tm_yday

s_path = os.path.join('sounds','nasty') 

files = list(os.listdir(s_path))

random.shuffle(files)

file_id = len(files) / day_of_year

file = files[file_id]

print(len(files))
# print(files)
print(day_of_year)
print(file_id)
print(file)