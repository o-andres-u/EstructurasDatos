def remove_last(array):
    if len(array) > 0:
        array.pop()


entry = input()
numbers = []
while entry != 'end':
    if entry.isdigit():
        numbers.append(int(entry))
    elif entry == 'M':
        print(*numbers, sep='')
    elif entry == 'D':
        remove_last(numbers)
    elif len(entry) > 1:
        command = entry.split()
        action = command[0]
        position = int(command[1])
        if position <= len(numbers):
            if position == 1:
                remove_last(numbers)
            elif action == 'B':
                numbers.pop(position * -1)
            elif action == 'C':
                numbers = numbers[0:(position * -1):1]
    entry = input()
