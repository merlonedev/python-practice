def asterisks(number):
    if number > 0:
        for n in range(number):
            print('*' * number)
    else:
        print('Use a value greater that 0')

asterisks(3)
