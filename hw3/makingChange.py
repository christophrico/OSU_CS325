# Assignment 3
# Christopher Rico
# CS325
# OSU ID: 933239746


import math
import timeit


#add two arrays together
def addArrays(array1, array2):
    for x in range(0, len(array1)):
        array1[x] += array2[x]



def makeChange(denoms, amount):
    coinAmountTracker = []
    currentDenomsCount = denoms

    #fills out a 2d array of possible coins per amount of money
    #values in the array are number of coins per denomination
    #and the last value in the array is the total number of coins
    for x in range(0, amount+1):
        coinAmountTracker.append([])
        #with an extra sub-array at the last index for tracking
        for y in range(1, len(denoms)+2):
            coinAmountTracker[x].append(0)


    #iterate through all numbers from 1 to the target coin amount
    for j in range(0, amount+1):
        amountLeft = j
        #iterate through all coin denominations starting with the largest
        for i in range(len(denoms)-1, -1, -1):
            if amountLeft > 0:
                currentCoin = denoms[i]

                if currentCoin <= amountLeft:
                    #calculates the number needed of the current coin
                    numCurrentCoin = math.floor(amountLeft / currentCoin)
                    # adds the number to the result array
                    coinAmountTracker[j][i] += int(numCurrentCoin)
                    #keeps a running total of how many coins we have used
                    coinAmountTracker[j][len(denoms)] += int(numCurrentCoin)
                    #calculates the remainder
                    amountLeft -= int(numCurrentCoin * currentCoin)
                    #looks for previous calculations using the amount in the remainder
                    #then adds the 2 arrays of results if found
                    if amountLeft > 0:
                        addArrays(coinAmountTracker[j], coinAmountTracker[amountLeft])
                        amountLeft = 0

    return (coinAmountTracker[amount])



def main():
    dataFile = open("amount.txt", "r")
    outFile = open("change.txt", "w")

    #on each set of denom/amount line pairs,
    #parse the data file into a denom array and amount
    for line in dataFile:
        denomArray = list(map(int, line.split()))
        amount = int(dataFile.next())

        #output denom/amount values to the change file
        for denom in denomArray:
            outFile.write(str(denom) + ' ')
        outFile.write('\n')
        outFile.write(str(amount))
        outFile.write('\n')

        #now get the change amount
        #uncomment the start and stop variables to report time
        start = timeit.default_timer()
        changeArray = makeChange(denomArray, amount)
        stop = timeit.default_timer()


        #write the change amount to the change file
        numCoins = 0
        for vals in changeArray[:-1]:
            outFile.write(str(vals) + ' ')
        #write the number of coins used to the change file
        outFile.write('\n')
        outFile.write(str(changeArray[-1]))
        outFile.write('\n')

    print stop - start

    dataFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
