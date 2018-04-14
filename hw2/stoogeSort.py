# Assignment 2
# Christopher Rico
# CS325
# OSU ID: 933239746

import math
import timeit

def stoogeSort(arr, idxLow, idxHi):
    n = idxHi - idxLow + 1

    if n == 2 and arr[idxLow] > arr[idxLow + 1]:
        holdMe = arr[idxLow]
        arr[idxLow] = arr[idxLow + 1]
        arr[idxLow + 1] = holdMe
    elif n > 2:
        m = int(math.ceil(2 * float(n) / 3))
        stoogeSort(arr, idxLow, m - 1 + idxLow)
        stoogeSort(arr, n - m + idxLow, idxHi)
        stoogeSort(arr, idxLow, m - 1 + idxLow)


def main():
    dataFile = open("data.txt", "r")
    outFile = open("stooge.out", "w")

    for line in dataFile:
        lineArr = list(map(int, line.split()))

        intArr = lineArr[1:]

        start = timeit.default_timer()
        stoogeSort(intArr, 0, len(intArr) - 1)
        stop = timeit.default_timer()

        for char in intArr:
            outFile.write(str(char) + ' ')

        outFile.write('\n')

    print stop - start

    dataFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
