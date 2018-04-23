import os
import sys
import commands

#put your n values you want to test in this array
valueArr = [50, 100, 200, 500, 1000, 2000, 4000, 5000, 10000, 20000, 50000]
amountArr = [110, 260, 320, 380, 430, 500, 670, 740, 890, 1100, 2170, 3850, 4000, 5980]

#get and store the input arguments
inputArgs = sys.argv

#create the file to output running times to
outFile = open("runTimes.csv", "w")


#write the column headers
outFile.write("N,A")
for z in inputArgs[1:]:
    outFile.write(',' + str(z) + ' (s)')


for x in valueArr:
    for d in amountArr:
        #generate the random file to be sorted
        randCall = "python randomNum.py " + str(x) + ' ' + str(d)
        os.system(randCall)

        outFile.write('\n' + str(x) + ' ' + str(d))

        for y in inputArgs[1:]:
            #print the algorithm being tested
            print("Testing " + str(y) + ' with N: ' + str(x) + ' and A: ' + str(d))

            #call the algorithm to be tested
            commandToRun = "python " + str(y)
            resultTime = commands.getoutput(commandToRun)

            #write the results to the output file
            outFile.write(',' + str(resultTime))

os.system("rm -f amount.txt change.txt")
outFile.close
print("All done!")
