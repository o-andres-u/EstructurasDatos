robots = set()
initial = int(input())
for index in range(1, initial+1):
    robots.add(index)

line = input()
while line != '#':
    entry = line.split()
    if entry[0] == 'new':
        new = int(entry[1]) + int(entry[2])
        while new in robots:
            new += 1
        robots.add(new)
    elif entry[0] == 'search':
        if int(entry[1]) in robots:
            print('existe')
        else:
            print('no existe')
    line = input()
