import random
import re
turns = 11
 # random select numbers
random_numbers = random.sample(range(1, 9), 4)
print(random_numbers)
print ('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.') 

# get user input
user_input = int(input('Input 4 digit code: '))
#string_input = str(user_input)
if len(str(user_input)) < 4 or user_input == ValueError:
    print('Please enter exactly 4 digits.')

user = str(user_input)
numbers = str(random_numbers)
c = 0

for i, j in zip(user,numbers):
    if i == j:
        c = c + 1
print(f'Number of correct digits in the correct place: {c}')

for i in user:
    if re.search(i,numbers):
        c = c + 1


if user is numbers:
    print('congrats')