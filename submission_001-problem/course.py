
import random
def create_set_of_topics():

    topics = sorted(['Introduction to Python','Tools of the Trade',
    'How to make decisions', 'How to repeat code', 'How to structure data', 
    'Functions','Modules'])
    course_topics = set(topics)
    print('Course Topics:',*topics, sep='\n* ')
    return topics, course_topics

def create_map_of_topics(course_topics):
    problem_list = ['Problem 1', 'Problem 2', 'Problem 3']
    problems = dict.fromkeys(course_topics, problem_list)
    print('Problems:')
    for key, value in problems.items():
        print('*',end=' ')
        print(key,end=' : ')
        print(*value,sep=', ')
    return problem_list


def create_tuple(topics,problem_list):   
    student_name = ['Mosa', 'Aurora', 'Adam',]
    status = ['[STARTED]', '[GRADED]', '[COMPLETED]',]
    print('Student Progress:')
    n = 0
    for n in range (0,len(student_name)):
        student_progress = (student_name[n], random.choice(topics), random.choice(problem_list), status[n])
        number = n + 1
        print(number,end='.')
        print(*student_progress, sep='-')
        n = n + 1


def sort_topics(topics):
    topics_sorted = sorted(topics)
   


def create_outline():
    topics,course_topics = create_set_of_topics()
    problem_list = create_map_of_topics(course_topics)
    create_tuple(topics,problem_list)
    sort_topics(topics)


if __name__ == "__main__":
    create_outline()
