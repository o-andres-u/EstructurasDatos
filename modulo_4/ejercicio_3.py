# 123
# 32145
# 541236
# 632154
from collections import deque

line = input()
dq = deque()
while line != '#':
    if line == 'inviertete':
        dq.appendleft(int(input()))
    else:
        dq.append(int(line))
    line = input()

print(dq)

#for i in range(len(dq)):
#    print(dq.popleft(), end='')
