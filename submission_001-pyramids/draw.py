

# TODO: Step 1 - get shape (it colan't be blank and must be a valid shape!)
def get_shape():
    shape_input = input('Shape?:')
    shape = shape_input.lower()
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = int(input("Height? "))
    return height


# TODO: Step 2
def draw_pyramid(height, outline):
    rows = height
    a = 0
    b = height -1
    n = height
    for r in range(1, n + 1):
        for c in range(1, (a+(n+1))):
            if outline:
                if r == n or c - r == n - 1 or c + r == n + 1:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if r + c <= n or c - r >= n:
                    print(" ",end="")
                else:
                    print("*",end="")
        a = a + 1
        print()

# TODO: Step 3
def draw_square(height, outline):
    n = height
    for row in range(1, n + 1):
        for col in range (1, n + 1):
            if outline:
                if row == 1 or row == n or col == 1 or col == n:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if row <= n or col <= n:
                    print("*",end="") 
        print()


# TODO: Step 4
def draw_triangle(height, outline):
    n = height
    a = 1
    for row in range(1, n + 1):
        for col in range(1, a + 1):
            if outline:
                if row == col or row == n or col == 1:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if col <= row:
                    print("*",end="") 
        a = a + 1
        print()

def draw_trapezium(height,outline):
    n = height
    count = 0
    a = n - 1  #this is a space counter
    row = 1
    while row <= n:
        space = a * " "
        if outline:
            print(space,end="")
            if row == 1 or row == n:
                print("*"*(n + count))
            elif a == n - row:
                print("*",end="")
                print((" ")*(n + count - 2),end="")
                print("*")
        else:
            print((space),end="")
            print(chr(42)* (n + count))
        a = a - 1
        count = count + 2
        row = row + 1

def draw_rectangle(height, outline):
    n = height
    m = height + 2
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if outline:
                if row == 1 or row == n or col == 1 or col == m:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if row <= n or col <= m:
                    print("*",end="")
        print()

def draw_rhombus(height, outline):
    row = 1
    col = 1
    b = height - 1 #space colounter
    while row <= height:
        space = b * " "
        if outline:
            print(space,end="")
            if row == 1 or row == height:
                print("*"*height,end="")
            else:
                print("*",end="")
                print(" " * (height-2),end="")
                print("*",end="")
        else:
            print(space,end="")
            print("*" * height,end="")
        b = b - 1
        row = row + 1
        print()    

    

# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
       draw_pyramid(height, outline)
    elif shape == "square":
        draw_square(height, outline)
    elif shape == "rhombus":
        draw_rhombus(height, outline)
    elif shape == "trapezium":
        draw_trapezium(height, outline)
    elif shape == "triangle":
        draw_triangle(height, outline)
    elif shape == "rectangle":
        draw_rectangle(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = str(input('Outline only? (y/N): ')).lower().strip()
    if outline == 'y':
        return True
    elif outline == 'n' or '': 
        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

