import random

Number = random.randint(1, 100)

user = -1

while user != Number:
    user = int(input('Guess a number from 1 to 100'))
    if user > Number:
        print('A number must be less')
    elif user < Number:
        print('A number must be more')
    else:
        print('You are guess a number')