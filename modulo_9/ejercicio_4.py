m = int(input())
line = input()
winners = set()
tickets = dict()
has_winner = False
while line != 'end':
    entry = line.split()
    if entry[0] == 'winner':
        winners.add(int(entry[1]))
    elif entry[0] == 'sms':
        number = int(entry[1])
        if number in tickets:
            tickets[number] += 1
        else:
            tickets[number] = 1
        if number in winners:
            has_winner = True
            print(number, int(m/(len(winners)*tickets[number])))
    line = input()

if not has_winner:
    print(0)
