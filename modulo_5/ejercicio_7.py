m = int(input())
number = int(input())
numbers = []
while number != 0:
    numbers.append(number)
    size = len(numbers)
    if size % m == 0:
        median = None
        numbers.sort()
        if size % 2 == 0:
            index = int(size//2)
            median = numbers[index] + numbers[index-1]
            if median % 2 == 0:
                median = median // 2
            else:
                median = str(median) + '/' + str(2)
        else:
            index = int(size//2)
            median = numbers[index]
        print(median)
    number = int(input())
