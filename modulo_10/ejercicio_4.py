numbers = []
N, T = input().split()
for i in range(int(N)):
    numbers.append(int(input()))

has_elements = False
sorted_numbers = sorted(numbers)
for i in range(len(sorted_numbers)):
    for j in range(i+1, len(sorted_numbers)):
        for k in range(j+1, len(sorted_numbers)):
            if int(T) == sorted_numbers[i] + sorted_numbers[j] + sorted_numbers[k]:
                has_elements = True
                print(sorted_numbers[i], sorted_numbers[j], sorted_numbers[k])
                break

if not has_elements:
    print('No hay trillizas')
