books = int(input())
isbns = tuple(map(int, input().split()))
ordered = sorted(isbns)
different = 0
previous = 0
for i in range(books):
    if previous != ordered[i]:
        different += 1
        previous = ordered[i]

print(different)
