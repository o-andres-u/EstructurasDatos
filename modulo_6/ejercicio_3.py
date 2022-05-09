import heapq

tests = int(input())
for test in range(tests):
    numbers = list(map(int, input().split()))
    numbers.pop()
    heapq.heapify(numbers)
    while len(numbers) > 2:
        first = heapq.heappop(numbers)
        second = heapq.heappop(numbers)
        heapq.heappush(numbers, first + second)
    print(heapq.heappop(numbers), heapq.heappop(numbers))
