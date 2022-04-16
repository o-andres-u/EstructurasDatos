# 123
# 32145
# 541236
# 632154
from collections import deque

line = input()
dq = deque()
while line != '#':
    if line == 'inviertete':
        length = len(dq)
        temp = [0] * length
        counter = 0
        for i in range(length):
            temp[counter] = dq.pop()
            counter += 1
        dq = deque(temp)
    else:
        number = int(line)
        dq.append(number)
    line = input()

for i in range(len(dq)):
    print(dq.popleft(), end='')
