import random

def correct_message(correct_place,not_correct_place):
    print(f'Number of correct digits in correct place:     {correct_place}')
    print(f'Number of correct digits not in correct place: {not_correct_place}')
    
def check_answer(code, answer):
    i = 0
    correct_place = 0
    not_correct_place = 0
    for item in code:
        if item == int(answer[i]):
            correct_place += 1
        elif int(answer[i]) in code:#str(i) in answer:
            not_correct_place += 1
        i += 1
      
        
    return correct_place, not_correct_place

def mastermind_code():
    code = []
    while len(code) < 4:
        number_to_add = random.randint(1, 8)
        if not number_to_add in code:
            code.append(number_to_add)
        else:
            continue
        
    return code

    # random_numbers = random.sample(range(1, 8), 4)
    # code = list(random_numbers)
    # return code

def instructions():
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def check_input(user_input):
    if len(user_input) != 4:
        print('Please enter exactly 4 digits.')
        return False
    
    if not user_input.isdigit():
        print('Please enter exactly 4 digits.')
        return False

    return True


def get_user_input():
    while True:
        user_input = input('Input 4 digit code: ')
        if check_input(user_input):
            break
        # else:
        #     continue
    #print(user_input)
    return user_input


def run_game():
    code = mastermind_code()
    instructions() 
    turns = 11
    while turns >= 0:
        answer = get_user_input()
        correct = check_answer(code, answer)
        if correct:
            correct_place, not_correct_place = check_answer(code, answer)
            # not_correct_place = check_answer(code, answer)
            correct_message(correct_place, not_correct_place)
        if correct_place == 4:
            my_code = ''.join(map(str, code))
            print('Congratulations! You are a codebreaker!', 'The code was: ' + my_code, sep='\n')
            break 
        print(f'Turns left: {turns}') 
        turns -= 1

if __name__ == "__main__":
    run_game()
