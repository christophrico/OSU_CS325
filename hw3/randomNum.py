import sys
import random
import math

numValues = int(sys.argv[1])
amount = int(sys.argv[2])
dataFile = open("amount.txt", "w")

numArray = [numValues]

for x in range(0, numValues-1):
    numArray.append(0)

for i in range(1, numValues):

    nextDenom = numArray[i-1] + random.randint(0, 4)
    if nextDenom > amount:
        nextDenom = numArray[i-1]
        
    numArray[i] = nextDenom

numArray[0] = 1

for values in numArray:
    dataFile.write(str(values) + ' ')


dataFile.write('\n')
dataFile.write(str(amount))
dataFile.write('\n')


dataFile.close()
