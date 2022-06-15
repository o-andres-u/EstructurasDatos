word = input()
words = dict()
while word != '#':
    words[word] = word
    word = input()
for i in words:
    col = i[0]
    for j in i[1:]:
        if col in words:
            if i[len(col):] in words:
                print(col + i[len(col):] + " = " + col + " + " + i[len(col):])
        col = col+j
