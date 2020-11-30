from io import StringIO
import sys

# list of valid command names
valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint', 'replay']

# list of valid movement commands
movements = ['forward', 'back', 'right', 'left', 'sprint']

#Empty history string
history = []

#Boolean for handling replay
to_do_replay = False

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#TODO: WE NEED TO DECIDE IF WE WANT TO PRE_POPULATE A SOLUTION HERE, OR GET STUDENT TO BUILD ON THEIR PREVIOUS SOLUTION.

def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        output(robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)
        

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    
    args = command.split(' ', 2)
    if len(args) == 2:
        return args[0], args[1], ''
    elif len(args) == 3:
        return args[0], args[1], args[2]
    return args[0], '', ''


def arg1_split(arg1):
    """
    Splits the first command to be able to separate the command that specify what interval of
    commands to repaly
    """
    arg1 = arg1.split('-')
    if len(arg1) == 0:
        return '',''
    elif len(arg1) == 1:
        return arg1[0],''
    elif len(arg1) == 2:
        return arg1[0],arg1[1]


def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1, arg2) = split_command_input(command)
    n = arg1.split('-')
    history = command_history(command)
    return command_name.lower() in valid_commands \
        and (len(arg1) == 0 or arg1.lower() == 'reversed' or is_int(arg1) or \
            arg1.lower() == 'silent' or (is_int(n[0]) and is_int(n[1]))) \
                and (len(arg2) == 0 or arg2.lower() == 'silent' or  is_int(arg2) or arg2.lower() == 'reversed')


def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    if update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    if update_position(-steps):
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)


def do_replay(robot_name,history,command_name, arg1, arg2):
    """
    repeats previous commands.
    1. Simple replay
    2. Replay x commands
    3. Replay an interval of commands
    4. Simple replay silent
    5. Replay x commands silently
    6. Simple replay reversed
    7. Replay x commands in reverse
    8. Replay x commands in reverse silently
    """
    a,b = arg1_split(arg1)
    to_do_replay = True
    if command_name == 'replay' and (len(arg1) == 0 or is_int(a) or len(arg1) == 2) and len(arg2) == 0 :
        if len(arg1) == 0 :
            replay = [handle_command(robot_name,command) for command in history]
            command_len = str(len(history))
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands.'
        elif is_int(a) and len(b) == 0:
            replay = [handle_command(robot_name,command) for command in history[-(int(a)):]]
            command_len = str(arg1[0])
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands.'
        elif is_int(a) and is_int(b):
            c = int(a) - int(b)
            replay = [handle_command(robot_name,command) for command in history[-(int(a)):-int(b)]]
            command_len = str(int(c))
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands.'
    

    elif command_name == 'replay' and (arg1 == 'silent' or is_int(a)) and \
        (len(arg2) == 0 or arg2 == 'silent' or is_int(arg2)):
        if len(arg2) == 0:
            original = sys.stdout
            new_string = StringIO()
            sys.stdout = new_string
            replay = [handle_command(robot_name,command) for command in history]
            command_len = str(len(history))
            sys.stdout = original
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands silently.'
        elif is_int(a):
            original = sys.stdout
            new_string = StringIO()
            sys.stdout = new_string
            replay = [handle_command(robot_name,command) for command in history[-(int(a)):]]
            command_len = str(a)
            sys.stdout = original
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands silently.'
        elif is_int(arg2):
            original = sys.stdout
            new_string = StringIO()
            sys.stdout = new_string
            replay = [handle_command(robot_name,command) for command in history[-(int(arg2)):]]
            sys.stdout = original
            return to_do_replay, ' > '+robot_name+' replayed ' +arg2+ ' commands silently.'


    elif command_name == 'replay' and arg1 == 'reversed' and (len(arg2) == 0 or is_int(arg2)):
        if len(arg2) ==0:
            reverse = [handle_command(robot_name,command) for command in history[::-1]]
            command_len = str(len(history))
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands in reverse.'
        elif is_int(arg2):
            new_history = [command for command in history[::-1]]
            reverse = [handle_command(robot_name,command) for command in new_history[:(int(arg2))]]
            command_len = str(arg2)
            return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands in reverse.'
    

    elif command_name == 'replay' and arg1 == 'reversed' and arg2 == 'silent':
        original = sys.stdout
        new_string = StringIO()
        sys.stdout = new_string
        reverse = [handle_command(robot_name,command) for command in history[::-1]]
        command_len = str(len(history))
        sys.stdout = original
        return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands in reverse silently.'
   
    elif command_name == 'replay' and is_int(arg1) and arg2 == 'reversed':
        new_history = [command for command in history[::-1]]
        reverse = [handle_command(robot_name,command) for command in new_history[-(int(arg1)):]]
        command_len = arg1
        return to_do_replay, ' > '+robot_name+' replayed ' +command_len+ ' commands in reverse.'  

def command_history(command):
    """
    Adds commands to a list and keeps track of all the commands the user has entered
    List is only appended if replay is not called
    """
    
    global history
    split_command = command.split()
    if split_command[0] in movements and to_do_replay == False:
        history.append(command)
    return history



def handle_command(robot_name, command):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """
    
    (command_name, arg1, arg2) = split_command_input(command)
    
    

    if command_name == 'off':
        return False
    elif command_name == 'help':
        (do_next, command_output) = do_help()
    elif command_name == 'forward':
        (do_next, command_output) = do_forward(robot_name, int(arg1))
    elif command_name == 'back':
        (do_next, command_output) = do_back(robot_name, int(arg1))
    elif command_name == 'right':
        (do_next, command_output) = do_right_turn(robot_name)
    elif command_name == 'left':
        (do_next, command_output) = do_left_turn(robot_name)
    elif command_name == 'sprint':
        (do_next, command_output) = do_sprint(robot_name, int(arg1))
    elif command_name == 'replay':
        (do_next, command_output) = do_replay(robot_name,history,command_name, arg1, arg2)
    print(command_output)
    show_position(robot_name)
    return do_next


def robot_start():
    """This is the entry point for starting my robot"""

    global position_x, position_y, current_direction_index, history, to_do_replay

    robot_name = get_robot_name()
    output(robot_name, "Hello kiddo!")
    history = []
    position_x = 0
    position_y = 0
    current_direction_index = 0
    to_do_replay = False

    command = get_command(robot_name)
    while handle_command(robot_name, command):
        command = get_command(robot_name)

    output(robot_name, "Shutting down..")


if __name__ == "__main__":
    robot_start()
