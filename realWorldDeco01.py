import time


def timing_function(some_function):
    '''
    Outputs the time a function takes
    to execute.
    '''

    def wrapper():
        time1 = time.time()
        some_function()
        time2 = time.time()
        return "Time it took to run the function: " + str((time1 - time2)) + '\n'
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nsum of all the numbers: " + str((sum(num_list))))

print(my_function())

