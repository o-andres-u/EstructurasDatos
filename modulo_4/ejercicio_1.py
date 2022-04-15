from collections import deque

statement = input()
deque = deque()
while statement != "terminamos":
    statement = statement.split()
    if statement[0] == "sube":
        deque.append(statement[1])
    elif statement[0] == "baja":
        deque.pop()
    statement = input()

while len(deque) > 0:
    print(deque.popleft())
