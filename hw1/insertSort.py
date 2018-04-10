# Assignment 1
# Christopher Rico
# CS325
# OSU ID: 933239746


import timeit

def insertionSort(arr):
    for j in xrange (1,len(arr)):
            key = arr[j]

            i = j - 1
            while (i > -1) and (arr[i] > key):
                arr[i + 1] = arr[i]
                i = i - 1

            arr[i + 1] = key

data_file = open("data.txt", "r");
out_file = open("insert.out", "w");

start = timeit.default_timer()

for line in data_file:
    lineArr = list(map(int,line.split()))

    intArr = lineArr[1:]

    insertionSort(intArr)

    for char in intArr:
        out_file.write(str(char) + ' ')

    out_file.write('\n')

stop = timeit.default_timer()
print ("Runtime is:")
print stop - start

data_file.close()
out_file.close()
