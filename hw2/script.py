import os
import sys
import commands

#put your n values you want to test in this array
valueArr = [100, 200, 400, 500]

#user-input algorithm to test
algo = sys.argv[1]


#create the file to output running times to
outFile = open("runningTime.csv", "w")
outFile.write('N,Runtime')


for x in valueArr:
    #generate the random file to be sorted
    randCall = "python randomNum.py " + str(x)
    os.system(randCall)

    #print the value being tested
    valPrint = "\nNum values: " + str(x)
    print(valPrint)

    #call the algorithm to be tested
    algoToRun = "python " + algo
    resultTime =  commands.getoutput(algoToRun)

    #write the results to the output file
    outFile.write('\n' + str(x) + ',' + resultTime)


outFile.close
print("Finished!")
