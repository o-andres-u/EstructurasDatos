# { [ ( ) ] } ;
# [ ] { } ( ) ;
# ( ) { [ } ] ;

# correcta
# correcta
# incorrecta

from collections import deque

N = int(input())
dq = deque()
for i in range(N):
    line = input().split()
    counter = 0
    while line[counter] != ';':
        character = line[counter]
        if len(dq) == 0 and (character == ')' or character == ']' or character == '}'):
            dq.append(character)
            break

        if character == ')' and dq[-1] == '(':
            dq.pop()
        elif character == ']' and dq[-1] == '[':
            dq.pop()
        elif character == '}' and dq[-1] == '{':
            dq.pop()
        else:
            dq.append(character)
        counter += 1

    if len(dq) == 0:
        print('correcta')
    else:
        print('incorrecta')
        dq.clear()
