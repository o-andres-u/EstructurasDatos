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


kms = int(input())
posts = tuple(map(int, input().split()))
posts = sorted(posts)
pairs = int(input())
for pair in range(pairs):
    entry = input().split()
    index_first = binary_search(posts, int(entry[0]))
    index_second = binary_search(posts, int(entry[1]))
    result = abs(index_first - index_second)
    print(f'{result} kms')
