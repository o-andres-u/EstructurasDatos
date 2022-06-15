entry = input()
felipe = set()
vanesa = set()
while entry != '#':
    pokemon = entry.split()
    if pokemon[0] == 'V':
        vanesa.add(int(pokemon[1]))
    else:
        felipe.add(int(pokemon[1]))
    entry = input()

print(len(felipe), len(vanesa), len(vanesa.union(felipe)))
