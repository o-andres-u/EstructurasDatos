def binary_search(local_array, value):
    start = 0
    end = len(local_array) - 1
    while start <= end:
        middle = int((start + end) / 2)
        if local_array[middle] == value:
            return middle
        elif local_array[middle] < value:
            start = middle + 1
        else:
            end = middle - 1
    return -1


size_array = int(input())
array = tuple(map(int, input().split()))
size_elements = int(input())
elements = tuple(map(int, input().split()))
accumulate = 0

for element in elements:
    index = binary_search(array, element)
    if index < size_array and array[index] == element:
        accumulate += index+1

print(accumulate)
