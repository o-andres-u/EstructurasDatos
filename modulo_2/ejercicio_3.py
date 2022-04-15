N = int(input())
numbers = tuple(map(int, input().split()))
acc = numbers[-1]
index = N - 2
while index >= 0:
    acc += numbers[index]
    print(acc)
    index -= 1
