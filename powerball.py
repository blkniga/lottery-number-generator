import random

n = (int)(input("Please input the number of balls you want: "))

# list to hold the 5 lottory numbers
numbers = list(range(n))


def randomPowerballs():
    ''' random lottory ball from 1-50 '''
    return random.randint(1, 50)


def powerball():
    ''' random powerball from 1-20 '''

    return random.randint(1, 20)


def lottoryNumbers():
    ''' a function for assigning random powerballs to the list & validates if the the ball is a one of one'''

    for number in range(0, n):
        numbers[number] = randomPowerballs()

    return numbers


def powerballValidator():
    ''' this method validates if whether the powerball is a one of one '''

    ok = lottoryNumbers()
    index = 0
    incrementStopper = 1

    for x in ok:

        for y in ok[incrementStopper:]:

            if x == y:

                ok[index] = randomPowerballs()
                incrementStopper = incrementStopper + 1

            else:

                incrementStopper = incrementStopper + 1

        index = index + 1
        incrementStopper = incrementStopper + 1

    return ok


print("The Lucky Numbers Are: ", powerballValidator())
print("The Powerball Is: ", powerball())
