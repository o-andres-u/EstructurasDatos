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
    line = input().split()
    size = int(line[0])
    number_P = int(line[1])
    elements = tuple(map(int, input().split()))
    primiConjunto = True
    for i in range(1, number_P+1):
        if number_P % i == 0:
            index = binary_search(elements, i)
            if index >= size or elements[index] != i:
                primiConjunto = False
                break

    if primiConjunto:
        print('Es PrimiConjunto')
    else:
        print('No es PrimiConjunto')
