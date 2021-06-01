import random

random_num = random.randint(1, 5)


def print_random_num():
    print('YOU HAVE JUST THREE TRIALS')
    
    user_input = int(input('Enter a random number : '))

    for i in range(2):
        print(i)
        if user_input != random_num:
            user_input = int(input('pick another number : '))
        else:
            print('YAY YOU WON')
    
    print('you out of time')


print_random_num()