from math import sqrt


def es_primo(numero):
    for index in range(2, int(sqrt(numero)) + 1):
        if numero % index == 0:
            return False
    return True


N = int(input())
for i in range(0, N):
    if es_primo(int(input())):
        print('primo')
    else:
        print('no primo')

# complejidad O(N*sqrt(N))
