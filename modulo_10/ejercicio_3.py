winners = dict()


def add_student(document):
    if document in winners:
        winners[document] += 1
    else:
        winners[document] = 1


if __name__ == '__main__':
    exercise_1 = int(input())
    for one in range(exercise_1):
        add_student(int(input()))
    exercise_2 = int(input())
    for two in range(exercise_2):
        add_student(int(input()))
    exercise_3 = int(input())
    for three in range(exercise_3):
        add_student(int(input()))
    exercise_4 = int(input())
    for four in range(exercise_4):
        add_student(int(input()))
    exercise_5 = int(input())
    for five in range(exercise_5):
        add_student(int(input()))

    students = len({key: value for (key, value) in winners.items() if value == 5})
    if students == 0:
        print('Nadie gana')
    else:
        print(int(1000000/students))
