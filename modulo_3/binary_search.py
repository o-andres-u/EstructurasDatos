def binary_search(array, value):
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if array[middle] == value:
            return middle
        elif array[middle] < value:
            start = middle + 1
        else:
            end = middle - 1
    return -1
