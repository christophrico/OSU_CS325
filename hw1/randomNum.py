import sys
import random

num_values = int(sys.argv[1])
data_file = open("data.txt", "w")

for _ in range(1, num_values):
    x = random.randint(0, 10000)
    data_file.write(str(x) + ' ')

data_file.close()
