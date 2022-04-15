M = int(input())
numbers = tuple(map(int, input().split(', ')))
C = int(input())
for i in range(0, C):
    N = int(input())
    major = 0
    minor = 0
    equal = 0
    for j in range(0, M):
        if numbers[j] > N:
            major += 1
        elif numbers[j] < N:
            minor += 1
        else:
            equal += 1
    print(f'mayores: {major}, menores: {minor}, iguales: {equal}')
