import os
import sys
import commands

#put your n values you want to test in this array
valueArr = [100, 200, 400, 500]

#get and store the input arguments
inputArgs = sys.argv

#create the file to output running times to
outFile = open("runTimes.csv", "w")


#write the column headers
outFile.write('N')
for z in inputArgs[1:]:
    outFile.write(',' + str(z) + ' (s)')


for x in valueArr:
    #generate the random file to be sorted
    randCall = "python randomNum.py " + str(x)
    os.system(randCall)

    outFile.write('\n' + str(x))

    for y in inputArgs[1:]:
        #print the algorithm being tested
        print("Testing " + str(y) + ' with N: ' + str(x))

        #call the algorithm to be tested
        commandToRun = "python " + str(y)
        resultTime = commands.getoutput(commandToRun)

        #write the results to the output file
        outFile.write(',' + str(resultTime))


outFile.close
print("All done!")
