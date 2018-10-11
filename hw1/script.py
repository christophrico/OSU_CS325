import os
import sys

#put your n values you want to test in this array
valueArr = [100, 200, 400, 500, 1000, 1500, 2000, 3000, 4000, 5000, 10000, 15000, 20000, 30000]

algo = sys.argv[1]

for x in valueArr:
    #generate the random file
    randCall = "python randomNum.py " + str(x)
    os.system(randCall)

    #print the number of values
    print("\nNum values:")
    print x

    #call the algorithm to be tested
    algoToRun = "python " + algo
    os.system(algoToRun)
