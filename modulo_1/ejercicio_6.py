A = int(input())
B = int(input())

if A <= B:
    counter = 1
    result = 0
    while A**counter <= B:
        print(A ** counter)
        counter += 1
