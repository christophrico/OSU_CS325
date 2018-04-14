import math

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

        stoogeSort(intArr, 0, len(intArr) - 1)

        for char in intArr:
            outFile.write(str(char) + ' ')

        outFile.write('\n')

    dataFile.close()
    outFile.close()

if __name__ == '__main__':
    main()
