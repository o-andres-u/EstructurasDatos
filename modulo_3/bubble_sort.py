def bubble_sort(array):
    size = len(array)
    for i in range(1, size):
        for j in range(0, size-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
