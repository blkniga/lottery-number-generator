import random

# list to hold the 6 lottory numbers
numbers = list(range(6))


def randomLottoBalls():
    ''' random lottory ball from 1-51 '''
    return random.randint(1, 51)


def lottoryNumbers():
    ''' a function for assigning random powerballs to the list & validates if the the ball is a one of onen'''

    for number in range(0, 6):
        numbers[number] = randomLottoBalls()

    return numbers


def powerballValidator():
    ''' this method validates if whether the powerball is a one of one '''

    ok = lottoryNumbers()
    index = 0
    incrementStopper = 1

    for x in ok:

        for y in ok[incrementStopper:]:

            if x == y:

                ok[index] = randomLottoBalls()
                incrementStopper = incrementStopper + 1

            else:

                incrementStopper = incrementStopper + 1

        index = index + 1
        incrementStopper = incrementStopper + 1

    return ok


print("The Lucky Numbers Are: ", powerballValidator())