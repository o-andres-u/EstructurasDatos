queue = []
entry = input()
while entry != 'fin':
    if entry == 'conteo':
        print(len(queue))
    else:
        values = entry.split()
        max_length = int(values[1])
        if len(queue) < max_length:
            queue.append(entry)
            if len(queue) > 1:
                previous = queue[-2]
                previous = previous.split()
                if len(queue) > int(previous[1]):
                    queue.pop(-2)

    entry = input()
