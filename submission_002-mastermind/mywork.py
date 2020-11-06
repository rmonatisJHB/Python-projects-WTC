import random
import re
turns = 11
 # random select numbers
random_numbers = random.sample(range(0, 9), 4)
print(random_numbers)
print ('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.') 

# get user input
user_input = int(input('Input 4 digit code: '))
#string_input = str(user_input)
if len(str(user_input)) < 4 or user_input == ValueError:
    print('Please enter exactly 4 digits.')
user = str(user_input)
numbers = str(random_numbers)
count = 0
# number check
for i in range (0,4):
    if user[i] in numbers:
        while True:
            if user[i] == numbers[i]:
                counter = user.count(i)
                print(f'Number of correct digits in the correct place: {counter}')
            elif user[i] in numbers:
                count = count + 1
                print(f'number of correct digits not in correct place: {count}')
            elif user == numbers:
                print('Congratulations! You are a codebreaker! \n The code was: {random_numbers}')
            i = i + 1
        else:
                print('Turns left: {turns}')

turns = turns - 1