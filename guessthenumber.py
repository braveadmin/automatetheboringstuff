import random

number = random.randint(1,20)
tries=0

print("I'm thinkting about a number between 1 and 20.")

while tries <= 6:
    
    print('take a guess:')

    guess = int(input())
    
    if guess < number:
        print('nope, higher.')
        tries = tries + 1

    elif guess > number:
        print('nope, lower.')
        tries = tries +1

    elif guess == number:
        print('you got it!!')
        break

if tries == 7:
    print('sorry bro, you have lost.')


