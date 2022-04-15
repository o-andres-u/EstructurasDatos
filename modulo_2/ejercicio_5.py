N = int(input())
A = input().split(', ')
B = input().split(', ')
score_A = 0
score_B = 0
for i in range(0, N):
    if A[i] == B[i]:
        continue
    elif A[i] == 'R' and B[i] == 'S' or A[i] == 'P' and B[i] == 'R' or A[i] == 'S' and B[i] == 'P':
        score_A += 1
    else:
        score_B += 1
print(f'{score_A} - {score_B}')
