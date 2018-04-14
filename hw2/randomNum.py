import sys
import random

num_values = int(sys.argv[1])
data_file = open("data.txt", "w")

data_file.write(str(num_values) + ' ')

for _ in range(0, num_values):
    x = random.randint(0, 5000)
    data_file.write(str(x) + ' ')

data_file.close()
