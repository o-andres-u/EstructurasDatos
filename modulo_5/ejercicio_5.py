queue = []
entry = input()
while entry != 'fin':
    if entry == 'conteo':
        print(len(queue))
    else:
        values = entry.split()
        max_length = int(values[1])
        if len(queue) < max_length:
            queue.append(max_length)
            for index in range(len(queue) - 1):
                if queue[index] < len(queue):
                    queue.pop(index)
    entry = input()
