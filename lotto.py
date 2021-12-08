import random

# list to hold the 6 lottory numbers
numbers = list(range(6))


def randomLottoBalls():
    ''' random lottory ball from 1-52 '''
    return random.randint(1, 52)


def lottoryNumbers():
    ''' a function for assigning random lottory balls to the list & validates if the lottory balls are one of one '''

    for number in range(0, 6):
        numbers[number] = randomLottoBalls()

    return numbers


def lottoryBallValidator():
    ''' this method validates if whether the random lottory ball is a one of one '''

    ok = lottoryNumbers()
    index = 0
    incrementStopper = 1

    for x in ok:

        for y in ok[incrementStopper:]:

            if x == y:

                # ok[index] = randomLottoBalls()
                # incrementStopper = incrementStopper + 1

                # the function must reloop until there are balls that are one of one (recursion at play, or am i wrong?)

                lottoryBallValidator()

            else:

                incrementStopper = incrementStopper + 1

        index = index + 1
        incrementStopper = incrementStopper + 1

    return ok


print("The Lucky Numbers Are: ", lottoryBallValidator())
