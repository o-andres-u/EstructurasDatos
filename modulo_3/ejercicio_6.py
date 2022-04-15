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


cases = int(input())
for case in range(cases):
    N = int(input())
    A = tuple(map(int, input().split(', ')))
    M = int(input())
    B = tuple(map(int, input().split(', ')))

    contained = True
    for element in B:
        index = binary_search(A, element)
        if index == -1:
            contained = False
            break

    if contained:
        print('B es subconjunto de A')
    else:
        print('B no es subconjunto de A')
