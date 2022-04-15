N = int(input())
numbers = tuple(map(int, input().split()))
M = int(input())

sliced = numbers[:M]
print(max(sliced))
