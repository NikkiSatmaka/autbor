def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    print(3 * number + 1)
    return 3 * number + 1


while True:  # Main program loop
    print('Enter number:')
    try:
        num = int(input())
        while num != 1:
            num = collatz(num)
        break
    except ValueError:
        print('Enter an integer.')
        continue
