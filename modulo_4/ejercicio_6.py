from collections import deque

cases = int(input())
for case in range(cases):
    disks = int(input())
    A = deque(range(disks, 0, -1))
    B = deque()
    C = deque()
    movement = input()
    message = None
    while movement != 'X X':
        movement = movement.split()
        origin = movement[0]
        destination = movement[1]

        if (origin == 'A' and len(A) == 0) or (origin == 'B' and len(B) == 0) or (origin == 'C' and len(C) == 0):
            message = 'secuencia invalida'

        elif origin == 'A' and destination == 'B':
            disk = A.pop()
            if len(B) > 0 and disk > B[-1]:
                message = 'secuencia invalida'
            else:
                B.append(disk)

        elif origin == 'A' and destination == 'C':
            disk = A.pop()
            if len(C) > 0 and disk > C[-1]:
                message = 'secuencia invalida'
            else:
                C.append(disk)

        elif origin == 'B' and destination == 'C':
            disk = B.pop()
            if len(C) > 0 and disk > C[-1]:
                message = 'secuencia invalida'
            else:
                C.append(disk)

        elif origin == 'B' and destination == 'A':
            disk = B.pop()
            if len(A) > 0 and disk > A[-1]:
                message = 'secuencia invalida'
            else:
                A.append(disk)

        elif origin == 'C' and destination == 'A':
            disk = C.pop()
            if len(A) > 0 and disk > A[-1]:
                message = 'secuencia invalida'
            else:
                A.append(disk)

        elif origin == 'C' and destination == 'B':
            disk = C.pop()
            if len(B) > 0 and disk > B[-1]:
                message = 'secuencia invalida'
            else:
                B.append(disk)

        movement = input()

    if len(A) == 0 and len(B) == 0 and len(C) == disks:
        message = 'soluciona la torre'
    elif message is None:
        message = 'no soluciona la torre'

    print(message)
