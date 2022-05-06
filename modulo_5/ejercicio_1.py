command = input()
numbers = list()
while command != 'E':
    command = command.split()
    if command[0] == 'A':
        numbers.append(int(command[1]))
    elif command[0] == 'M':
        number = int(command[1])
        temp = filter(lambda x: (x % number == 0), numbers)
        print(sum(temp))
    command = input()
