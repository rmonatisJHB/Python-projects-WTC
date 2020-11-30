import turtle
from world import obstacles 
screen = turtle.Screen()
screen.setworldcoordinates(-300,-250,300,250)
pegasus = turtle.Turtle()
pegasus.pensize(2)
pegasus.pencolor("red")
# screen.setworldcoordinates


# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

blocked = False

#draw the bounadries
pegasus.penup()
pegasus.goto(100,200)
pegasus.pendown()
pegasus.rt(90)
pegasus.forward(400)
pegasus.rt(90)
pegasus.forward(200)
pegasus.rt(90)
pegasus.forward(400)
pegasus.rt(90)
pegasus.forward(200)
pegasus.penup()
pegasus.goto(0,0)
pegasus.lt(90)
# screen.exitonclick() 


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

    global position_x, position_y, blocked
    global blocked
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
        if not obstacles.is_path_blocked(position_x,position_y, new_x,new_y):
            position_x = new_x
            position_y = new_y
            return True
        else:
            blocked = True
            return False
    
    blocked = False
    return False


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    
    if update_position(steps):
        pegasus.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif blocked == True:
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
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
        pegasus.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif blocked == True :
        return True, ''+robot_name+': Sorry, there is an obstacle in the way.'
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
    pegasus.right(90)

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
    pegasus.left(90)


    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2)
     + .. + 1 number of steps, in iterations
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

def draw_obstacles():
    """
    create the specific number of obstacles
    """
    pegasus.color("#e3751b","#e3751b")
    for i in obstacles.get_obstacles():
        pegasus.goto(i[0])
        pegasus.pendown()
        pegasus.begin_fill()
        for j in range(4):
            pegasus.forward(4)
            pegasus.right(90)
        pegasus.end_fill()
        pegasus.penup()
    pegasus.goto(0,0)

def clear_obs():
    """
    resets the obstacle list
    """
    obstacles.obs_list =[]