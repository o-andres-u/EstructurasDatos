import heapq

tests = int(input())
for test in range(tests):
    total_numbers = int(input())
    numbers = list(map(int, input().split()))
    heapq.heapify(numbers)
    x = '0'
    y = '0'
    while len(numbers) > 0:
        x += str(heapq.heappop(numbers))
        if len(numbers) > 0:
            y += str(heapq.heappop(numbers))
    print(int(x) + int(y))
