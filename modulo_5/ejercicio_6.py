total_students, k_variable = [int(x) for x in input().split()]

numbers = list(range(1, total_students + 1))

index = 0
for case in range(total_students - 1):
    index = ((index + k_variable) % len(numbers)) - 1
    if index < 0:
        index += len(numbers)

    number = numbers.pop(index)

    k_variable = number % len(numbers)
    if k_variable == 0:
        k_variable = 1

print(numbers.pop())
