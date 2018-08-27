#
# Cows and Bulls
#
# Exercise from https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
#
import random


def countCows(number, guess) -> int:
    """
    Count the number of digits in the correct position
    :param number: random number user is trying to guess
    :param guess: user supplied guess
    :return: number of matches, 0-4
    """
    cowsFound = 0
    for index in range(4):
        if number[index] == guess[index]:
            cowsFound += 1
    return cowsFound


def countBulls(number, guess) -> int:
    """
    Count the number of digits that match, but which are not in the correct location.
    :param number: random number user is trying to guess
    :param guess: user supplied guess
    :return:
    """
    bullsFound = 0
    numberList = removeMatchingDigits(guess, number)
    guessList = removeMatchingDigits(number, guess)

    for index in range(4):
        digit = guessList[index]
        if digit != " " and numberList.count(digit) > 0:
            digitIndex = numberList.index(digit)
            numberList[digitIndex] = " "
            bullsFound += 1

    return bullsFound


def removeMatchingDigits(guess, number) -> list:
    """
    Convert the number into a list and replace any digit that matches a digit in the guess, at the same location, with a space.
    :param guess: to match against number
    :param number: to remove digits from
    :return: a 4 element list
    """
    numberList = list(number)
    for index in range(4):
        if numberList[index] == guess[index]:
            numberList[index] = " "
    return numberList


if __name__ == "__main__":
    # Generate a random number between 0 -> 9999 and convert it into a string 4 characters long
    randomNumber = "{:0<4}".format(random.randint(1, 9999))

    cows = 0
    while cows < 4:
        rawInput = input("Enter a number :\n")
        formattedGuess = "{:0<4}".format(rawInput)

        cows = countCows(randomNumber, formattedGuess)
        bulls = countBulls(randomNumber, formattedGuess)

        print(cows, " cows, ", bulls, " bulls")

    print("\nCorrect !!!")
