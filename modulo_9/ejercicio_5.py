entry = input().split()
votes = dict()
while entry[0] != '0' and entry[1] != '0':
    citizen = int(entry[0])
    candidate = int(entry[1])
    if citizen in votes:
        votes[citizen] = 0
    else:
        votes[citizen] = candidate
    entry = input().split()

filtered_votes = {key: value for (key, value) in votes.items() if value != 0}
candidates = {}
for vote in filtered_votes.values():
    if vote in candidates:
        candidates[vote] += 1
    else:
        candidates[vote] = 1
sorted_by_key = dict(sorted(candidates.items(), key=lambda item: item[0], reverse=True))
sorted_by_value = dict(sorted(sorted_by_key.items(), key=lambda item: item[1], reverse=True))

for k, v in sorted_by_value.items():
    print(k, v)
