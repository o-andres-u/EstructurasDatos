N = int(input())
positives = 0
negatives = 0
for i in range(0, N):
    number = int(input())
    if number < 0:
        negatives += number
    elif number > 0:
        positives += number
print(f'positivos {positives}, negativos {negatives}')
