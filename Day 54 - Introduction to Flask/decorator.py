import time
import math


# decorator function which output time take taken by function to complete execution
def timeTakenByFunction(func):

    # argument can be added like this if function takes any argument
    def inner(*args, **kwargs):

        startTime = time.time() # starting time before function execution

        returnValue = func(*args, **kwargs) # executing the function

        endTime = time.time() # time after function execution completed

        timeTaken = endTime - startTime

        print(f'Time taken by function ({func.__name__}) is {timeTaken}s.')

        return returnValue

    return inner


@timeTakenByFunction
def printMessage(message):
    print(message)


@timeTakenByFunction
def getFact(number):
    time.sleep(2) # for 2sec delay
    return math.factorial(number)

@timeTakenByFunction
def shortFunction():
    for i in range(100000):
        i*i

# similar to timeTakenByFunction(longFunction)()
@timeTakenByFunction
def longFunction():
    for i in range(10000000):
        i*i

printMessage('Hello World')
getFact(100)
shortFunction()
longFunction()