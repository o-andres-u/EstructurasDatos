N = int(input())
SO = tuple(map(int, input().split(', ')))
LAR = tuple(map(int, input().split(', ')))
IS = tuple(map(int, input().split(', ')))

score_SO = 0
score_LAR = 0
score_IS = 0

for index in range(0, N):
    if SO[index] % 2 == 0 and (SO[index] + LAR[index] + IS[index]) % 2 == 0 or SO[index] % 2 != 0 and (SO[index] + LAR[index] + IS[index]) % 2 != 0:
        score_SO += 1
    if LAR[index] % 2 == 0 and (SO[index] + LAR[index] + IS[index]) % 2 == 0 or LAR[index] % 2 != 0 and (SO[index] + LAR[index] + IS[index]) % 2 != 0:
        score_LAR += 1
    if IS[index] % 2 == 0 and (SO[index] + LAR[index] + IS[index]) % 2 == 0 or IS[index] % 2 != 0 and (SO[index] + LAR[index] + IS[index]) % 2 != 0:
        score_IS += 1

print(f'SO:{score_SO}, LAR:{score_LAR}, IS:{score_IS}')
