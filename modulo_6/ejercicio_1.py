import heapq

queue = []
heapq.heapify(queue)
entry = input()
last_element = None
while entry != 'end':
    if entry == 'sig' and len(queue) > 0:
        last_element = heapq.heappop(queue)
    elif entry.isdigit():
        heapq.heappush(queue, int(entry))
    entry = input()
print(last_element)
