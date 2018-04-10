# Assignment 1
# Christopher Rico
# CS325
# OSU ID: 933239746


import timeit

def merge_sort(array):
    array_size = len(array)

    if array_size == 1 or array_size == 0:
        return array

    array_split = array_size / 2

    num1 = merge_sort(array[:array_split])
    num2 = merge_sort(array[array_split:])

    return merge(num1, num2)


def merge(array1, array2):
    new_array = []
    array1_length = len(array1)
    array2_length = len(array2)

    while array1_length != 0 and array2_length != 0:

        if array1[0] < array2[0]:
            new_array.append(array1.pop(0))
        else:
            new_array.append(array2.pop(0))

        array1_length = len(array1)
        array2_length = len(array2)


    if array1_length == 0:
        new_array += array2
    else:
        new_array += array1

    return new_array


def main():
    data_file = open("data.txt", "r")
    out_file = open("merge.out", "w")

    start = timeit.default_timer()

    for line in data_file:
        line_arr = list(map(int, line.split()))

        int_arr = line_arr[1:]

        sorted_arr = merge_sort(int_arr)

        for char in sorted_arr:
            out_file.write(str(char) + ' ')

        out_file.write('\n')

    stop = timeit.default_timer()

    print ("Runtime is:")
    print stop - start

    data_file.close()
    out_file.close()


if __name__ == "__main__":
    main()
