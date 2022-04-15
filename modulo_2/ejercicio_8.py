C = int(input())
for case in range(0, C):
    N = int(input())
    values = tuple(map(int, input().split()))
    jump = 0
    index = 0
    indexes = tuple()
    while 0 <= index < N and index not in indexes:  # O(N²)
        # indexes.append(index) # casi O(1) esto sería con listas
        indexes += (index,)  # con tuplas, pero sería O(n)
        index += values[index]
        jump += 1
    print(jump)

# O(C*N*N)
