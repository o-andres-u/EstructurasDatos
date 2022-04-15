N = int(input())
values = input().split(', ')
values = tuple(map(int, values))
M = int(input())
for i in range(0, M):
    interval = input().split()
    a = int(interval[0])
    b = int(interval[1])
    counter = 0
    for j in range(0, N):
        if a <= values[j] <= b:
            counter += 1
    print(counter)
