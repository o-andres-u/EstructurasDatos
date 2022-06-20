numbers = []
N, T = input().split()
for i in range(int(N)):
    numbers.append(int(input()))

N = int(N)
T = int(T)

has_elements = False
elements = []
for i in range(N - 1):
    s = set()
    for j in range(i+1, N):
        x = T-(numbers[i] + numbers[j])
        if x in s:
            elements.append(sorted([x, numbers[i], numbers[j]]))
            has_elements = True
        else:
            s.add(numbers[j])

if not has_elements:
    print('No hay trillizas')
else:
    elements.sort()
    for element in elements:
        print(*element, sep=' ')

# Solved with https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
