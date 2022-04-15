N = int(input())
characters = input().split(', ')
left = 0
right = N - 1
for i in range(0, N):
    if i % 2 == 0:
        print(characters[left], end='')
        left += 1
    else:
        print(characters[right], end='')
        right -= 1
