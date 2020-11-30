import random



obs_list = []

def get_obstacles():
    """
    create random number of obstacles
    """
    global obs_list
    obs_list = []
    number_obs = random.randint(1,10)
    for i in range(number_obs):
        (rand_x, rand_y)= (random.randint(-100,96), random.randint(-200,196))
        obs_list.append([(rand_x,rand_y)])
    return obs_list


def is_position_blocked(x,y):
    """
    checks if the position where the robot is moving to is blocked or not
    """
    global obs_list
    blocked = False
    for i in obs_list:
        if (i[0][0]) <= x <= (i[0][0]+ 4) and (i[0][1]) <= y <= (i[0][1]+4):
            blocked = True
            return blocked


def is_path_blocked(x1,y1,x2,y2):
    """
    x1 is the current position; x2 is where we are trying to move to along the x-axis
    y1 is the current position; y2 is where we are trying to move to along the y-axis
    """
    blocked = False

    if y1 == y2:
        while x1 <= x2:
            if is_position_blocked(x1,y1):
                blocked = True
                break
            x1 += 1
        while x1 >= x2:
            if is_position_blocked(x1,y1):
                blocked = True
                break
            x1 -=1
    elif x1 == x2:
        while y1 <= y2:
            if is_position_blocked(x1,y1):
                blocked = True
                break
            y1 += 1
        while y1 >= y2:
            if is_position_blocked(x1,y1):
                blocked = True
                break
            y1 -=1
    return  blocked
            






