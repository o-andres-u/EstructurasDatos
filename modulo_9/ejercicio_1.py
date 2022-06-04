documents = set()
document = int(input())
rodriguez, gomez, gonzalez = 0, 0, 0
while document != 0:
    if document not in documents:
        documents.add(document)
        if document % 3 == 0:
            rodriguez += 1
        elif document % 3 == 1:
            gomez += 1
        elif document % 3 == 2:
            gonzalez += 1
    document = int(input())

print('Rodriguez', rodriguez)
print('Gomez', gomez)
print('Gonzalez', gonzalez)
