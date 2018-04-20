# Assignment 3
# Christopher Rico
# CS325
# OSU ID: 933239746


import math
import timeit


#add two arrays together
def addArrays(array1, array2):
    for x in range(0, len(array1)):
        array1[x] += int(array2[x])



def makeChange(denoms, amount):
    coinAmountTracker = []
    currentDenomsCount = denoms

    #fills out a 2d array of possible coins per amount of money
    for x in range(0, amount):
        coinAmountTracker.append([])
        for y in range(1, len(denoms)+1):
            coinAmountTracker[x].append(0)


    #iterate through all numbers from 1 to the target coin amount
    for j in range(0, amount):
        amountLeft = j
        #iterate through all coin denominations starting with the largest
        for i in range(len(denoms)-1, -1, -1):
            print("Iteration " + str(j+1) + ' ' + str(i+1))
            print("And the coinAmountTracker: ")
            print(coinAmountTracker)
            if amountLeft > 0:
                currentCoin = denoms[i]
                print("Current coin is " + str(currentCoin))

                if currentCoin <= amountLeft:
                    #calculates the number needed of the current coin
                    numCurrentCoin = math.floor(amountLeft / currentCoin)
                    print("This is how many of these coins we need to make change " + str(numCurrentCoin))
                    # adds the number to the result array
                    coinAmountTracker[j][i] += int(numCurrentCoin)
                    #keeps a running total on the subarray
                    coinAmountTracker[j][len(denoms)-1] += int(numCurrentCoin)
                    #calculates the remainder
                    amountLeft -= int(numCurrentCoin * currentCoin)
                    print("The remainder is " + str(amountLeft))
                    #looks for previous calculations using the amount in the remainder
                    #then adds the 2 arrays of results if found
                    if amountLeft > 0:
                        addArrays(coinAmountTracker[j], coinAmountTracker[amountLeft])
                        amountLeft = 0

    return (coinAmountTracker[int(amount/2)])



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

        #write the change amount and num coins to the change file
        numCoins = 0
        for vals in changeArray:
            outFile.write(str(vals) + ' ')
            #calculate the minimum number of coins used
            numCoins += vals
        outFile.write('\n')
        outFile.write(str(numCoins))
        outFile.write('\n')

    print stop - start

    dataFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
