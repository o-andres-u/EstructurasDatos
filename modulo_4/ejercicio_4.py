# 5 4 3 2 1 31
# 5 4 3 2 16
# 5 4 3 9
# 5 4 6
# 5 5
# 5
from collections import deque

dq = deque()
entry = int(input())
while entry != 0:
    dq.append(entry)
    while len(dq) >= 2 and (dq[-1] + dq[-2]) % 2 == 0:
        first = dq.pop()
        second = dq.pop()
        dq.append(int((first + second) / 2))
    entry = int(input())

print(len(dq), dq[-1])
