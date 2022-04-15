cases = int(input())
for case in range(cases):
    size = int(input())
    array_A = list(map(int, input().split(', ')))
    sum_A = sum(array_A)
    array_B = list(map(int, input().split(', ')))
    sum_B = sum(array_B)
    if sum_A == sum_B:
        print('A y B son identicos')
    else:
        print('A y B son diferentes')
