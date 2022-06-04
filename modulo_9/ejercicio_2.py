entry = input()
born = set()
dead = set()
while entry != 'E':
    entry = entry.split()
    event, document = entry[0], int(entry[1])
    if event == 'B' and document not in dead:
        born.add(document)
    elif event == 'D' and document in born:
        born.remove(document)
        dead.add(document)
    elif event == 'R' and document in dead:
        born.add(document)
    entry = input()
print(len(born))
