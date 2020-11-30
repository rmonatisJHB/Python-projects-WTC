
def turn_left(direction):
    """Turns the robot left"""

    if direction == "north":
        direction = "west"
    elif direction == "west":
        direction = "south"
    elif direction == "south":
        direction = "east"
    elif direction == "east":
        direction = "north"
    
    return direction


def turn_right(direction):
    """Turns the robot right"""

    if direction == "north":
        direction = "east"
    elif direction == "east":
        direction = "south"
    elif direction == "south":
        direction = "west"
    elif direction == "west":
        direction = "north"
 
    return direction


def move_back(direction,position, command):
    """ moves the robot back"""
    
    if direction == "north":
        position[1] -= int(command[1])
    elif direction == "south":
        position[1] += int(command[1])
    elif direction == "east":
        position[0] -= int(command[1])
    elif direction == "west":
        position[0] += int(command[1])
    return position


def move_forward(direction, position, command):
    """moves the robot forward"""

    if direction == "north":
        position[1] += int(command[1])
    elif direction == "south":
        position[1] -= int(command[1])
    elif direction == "east":
        position[0] += int(command[1])
    elif direction == "west":
        position[0] -= int(command[1])
    return position


def sprint(command,robot_name):
    """The sprint command allows the robot to move further than the specified steps"""

    if command == 0:
        return command
    else:
        print(f" > {robot_name} moved forward by {command} steps.")
        return command + sprint(command - 1,robot_name)


def robot_steps(robot_name, command):
    """Prints out the steps that the robot took"""

    print(f" > {robot_name} moved {command[0]} by {command[1]} steps.")

def robot_position(robot_name, position):
    """Prints out the position of the robot"""

    print(f" > {robot_name} now at position ({position[0]},{position[1]}).")


def robot_turns(robot_name,command):
    """Prints out the turns taken by the robot"""

    print(f" > {robot_name} turned {command[0]}.")

def handle_command(command,robot_name,direction,position):
    """Handles every command that the user inputs and returns the direction"""
    
    if command[0] == "help":
        handle_help()
        
    elif command[0] == "forward":
        position = move_forward(direction, position, command)
        position = check_area(direction,command,robot_name,position)
        
             
    elif command[0] == "back":
        position = move_back(direction, position, command)
        position = check_area(direction,command,robot_name,position)  
   
    elif command[0] == "right":
        direction = turn_right(direction)
        robot_turns(robot_name,command)
        robot_position(robot_name, position)     

    elif command[0] == "left":
        direction = turn_left(direction)
        robot_turns(robot_name,command)
        robot_position(robot_name, position)
    
    elif command[0] == "sprint":
        command[1] = sprint(int(command[1]),robot_name)
        move_forward(direction,position,command)
        position = check_area(direction,command,robot_name,position)
    
    return direction   


def check_area(direction,command,robot_name,position):
    """Check if the steps are within the boundaries set for the robot"""

    if direction == "north":
        p = int(command[1])
        y = int(position[1])
        if y >= -200 and y <= 200:
            if command[0] == "sprint":
                robot_position(robot_name, position)
            else:    
                robot_steps(robot_name, command)
                robot_position(robot_name, position)
        elif y < - 200 or y > 200:
            print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
            if command[0] == "forward":
                position[1] =  (y - p)
            elif command[0] == "back":
                position[1] =  (y + p)
            robot_position(robot_name, position)
            

    elif direction == "south":
        p = int(command[1])
        y = int(position[1])
        if y >= -200 and y <= 200:
            if command[0] == "sprint":
                robot_position(robot_name, position)
            else:    
                robot_steps(robot_name, command)
                robot_position(robot_name, position)
        elif y < - 200 or y > 200:
            print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
            if command[0] == "forward":
                position[1] =  (y + p)
            elif command[0] == "back":
                position[1] =  (y - p)
            robot_position(robot_name, position) 
            
    elif direction == "east":
        p = int(command[1])
        x = int(position[0])
        if x >= -100 and x <= 100:
            if command[0] == "sprint":
                robot_position(robot_name, position)
            else:    
                robot_steps(robot_name, command)
                robot_position(robot_name, position)
        elif x < -100 or x > 100:
            print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
            if command[0] == "forward":
                position[0] = (x - p)
            elif command[0] == "back":
                position[0] = (x + p)   
            robot_position(robot_name, position) 
    
    elif direction == "west":
        p = int(command[1])
        x = int(position[0])
        if x >= -100 and x <= 100:
            if command[0] == "sprint":
                robot_position(robot_name, position)
            else:    
                robot_steps(robot_name, command)
                robot_position(robot_name, position)
        elif x < -100 or x > 100:
            print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")
            if command[0] == "forward":
                position[0] = (x + p)  
            elif command[0] == "back":
                position[0] = (x - p)
            robot_position(robot_name, position) 

    return position

def handle_help():
    """Handle the help command"""

    print("I can understand these commands:\n"
    "OFF  - Shut down robot\n"
    "HELP - provide information about commands\n"
    "FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'\n"
    "BACK - move backward by specified number of steps, e.g. 'BACK 10'\n"
    "RIGHT - turn right by 90 degrees\n"
    "LEFT - turn left by 90 degrees\n"
    "SPRINT - sprint forward according to a formula\n")


def check_command(robot_command,robot_name,command):
    """Checks if the command from the user is a valid command"""

    command_lst = ["off", "help","forward", "back", "right", "left", "sprint"]
    if  command[0] in command_lst and (len(command) == 1 or command[1].isdigit()):
        return command
    else:
        print(f"{robot_name}: Sorry, I did not understand '{robot_command}'.")


def get_command(robot_name):
    """Handles user input by getting a command from user and validating the command"""

    robot_command = input(f"{robot_name}: What must I do next? ")
    command = robot_command.lower().split()
    check_command(robot_command,robot_name,command)
    return robot_command, command


def name_robot():
    """Get the name of the robot from the player"""

    robot_name = input('What do you want to name your robot? ')
    return robot_name


def robot_start():
    """This is the entry function, do not change"""
    robot_name = name_robot()
    while len(robot_name) == 0:
        robot_name = name_robot()
    print(f"{robot_name}: Hello kiddo!")
    position = [0,0] 
    direction = "north"
    robot_command,command = get_command(robot_name)
    
    while command[0] != "off":
        direction = handle_command(command, robot_name, direction,position)
        robot_command,command = get_command(robot_name)
    else:
        print(f"{robot_name}: Shutting down..")


if __name__ == "__main__":
    robot_start()
