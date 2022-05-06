def populate_integers(max_value):
    array = []
    for number in range(1, max_value + 1):
        array.append(number)
    return array


def remove_integers(array):
    iteration = 1
    while iteration + 1 <= len(array):
        index = 0
        while index < len(array):
            array.pop(index)
            index += iteration
        iteration += 1


tests = int(input())
test = 1
while test <= tests:
    value = int(input())
    integers = populate_integers(value)
    remove_integers(integers)
    print(*integers)
    test += 1
