import heapq

A = []
B = []
C = []

points_A = 0
points_B = 0
points_C = 0

heapq.heapify(A)
heapq.heapify(B)
heapq.heapify(C)

entry = input()
while entry != 'fin del juego':
    if entry == 'menores':
        a = 1001
        b = 1001
        c = 1001
        if len(A) == 0 and len(B) == 0 and len(C) == 0:
            entry = input()
            continue

        if len(A) > 0:
            a = heapq.heappop(A)
        if len(B) > 0:
            b = heapq.heappop(B)
        if len(C) > 0:
            c = heapq.heappop(C)

        if a < b and a < c:
            points_A += 1
        elif b < a and b < c:
            points_B += 1
        elif c < b and c < a:
            points_C += 1
        elif a == b == c:
            points_A += 1
            points_B += 1
            points_C += 1
        elif a == b:
            points_A += 1
            points_B += 1
        elif a == c:
            points_A += 1
            points_C += 1
        elif b == c:
            points_B += 1
            points_C += 1
    else:
        values = entry.split()
        number = int(values[1])
        if values[0] == 'A':
            heapq.heappush(A, number)
        elif values[0] == 'B':
            heapq.heappush(B, number)
        else:
            heapq.heappush(C, number)
    entry = input()

print('Equipo A:', points_A)
print('Equipo B:', points_B)
print('Equipo C:', points_C)
