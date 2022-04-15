def select_sort(array):
    for i in range(len(array)):
        index_minor = i
        for j in range(i+1, len(array)):
            if array[j] < array[index_minor]:
                index_minor = j
        array[i], array[index_minor] = array[index_minor], array[i]


N = int(input())
numbers = list(map(int, input().split()))
select_sort(numbers)

Q = int(input())
for cases in range(Q):
    k = int(input())
    print(numbers[k-1])
