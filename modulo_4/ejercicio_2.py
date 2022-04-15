from collections import deque

line = input().split()
buyers = int(line[0])
tickets = int(line[1])
dq = deque()
for cases in range(buyers):
    entry = input().split()
    record = (entry[0], int(entry[1]))
    dq.append(record)

buyer_document = None
buyer_tickets = None
shop_counter = 0
while len(dq) > 0 and tickets > 0:
    buyer = dq.popleft()
    buyer_document = buyer[0]
    buyer_tickets = buyer[1]
    tickets -= buyer_tickets
    shop_counter += 1

    if shop_counter % 5 != 0:
        dq.append(buyer)
if tickets > 0:
    print("quedaron boletas disponibles")
else:
    print(buyer_document, buyer_tickets + tickets)
