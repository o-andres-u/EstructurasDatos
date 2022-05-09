entry = input().split()
friends = int(entry[0])
minutes = int(entry[1])
time = int(entry[2])

documents = []
removed = []
for friend in range(friends):
    documents.append(int(input()))

turns = int(minutes / time)

index = 0
counter = 0
while len(documents) > 1:
    counter += 1
    if counter == 8:
        counter = 0
        removed.append(documents.pop(index))
    else:
        index += 1
    index %= len(documents)

print(documents[0])
for i in range(turns-1):
    print(removed.pop())
