import heapq
pq = []
heapq.heapify(pq)
s = input()
while s != 'end':
    if s.isdigit():
        heapq.heappush(pq, int(s)*-1)
    if s == 's':
        print(heapq.heappop(pq)*-1)
    s = input()
