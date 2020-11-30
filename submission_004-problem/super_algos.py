
# element = [8,6,1,0,3,7]

def check_type(element, d_type):

    results = False
    for i in element:
        if type(i) == d_type:
            results = True
        else:
            results = False
            break
    return results

def find_min(element):
    """TODO: complete for Step 1"""
    
    if check_type(element,int) == True and len(element) > 0:
        if len(element) == 1:
            return element[0]
        if element[0] < element[1]:
            element.append(element[0])
            return find_min(element[1:])
        else:
            return find_min(element[1:])
    else:
        return(-1)    

    

def sum_all(element):
    """TODO: complete for Step 2"""
    if check_type(element,int) == True and len(element) > 0:
        if len(element) == 1:
            return element[0]
        else:
            last_num = element.pop()
            return last_num + sum_all(element)
    else:
        return(-1)


def print_possible_strings(character_set, prefix, length, n):
    if n == 0:
        print(prefix)
        return
    for i in range(length):
        current_prefix = prefix + character_set[i]
        print_possible_strings(character_set, current_prefix, length, (n -1))
    return


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    if check_type(character_set,str) == True and len(character_set) >= 1: 
        length = len(character_set)
        return print_possible_strings(character_set, "", length, n)
    else:
        return([])


if __name__ == "__main__":
    element = [8,6,1,3,7,0,13,]
    print (find_min(element))
    print (sum_all(element))
    n = 3
    character_set = ['a','b']
    print (find_possible_strings(character_set,n))