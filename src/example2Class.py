#
# Cows and Bulls exercise extended to use a class
#
# Exercise from https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
#
import random


class CowsBullsGame:

    def __init__(self, number):
        self.randomNumber = number
        self.cowsFound = 0
        self.bullsFound = 0

    def count_cows(self, guess):
        """
        Count the number of digits in the correct position
        :param guess: user supplied guess
        """

        self.cowsFound = 0
        for index in range(4):
            if self.randomNumber[index] == guess[index]:
                self.cowsFound += 1

    def count_bulls(self, guess):
        """
        Count the number of digits that match, but which are not in the correct location.
        :param guess: user supplied guess
        """
        self.bullsFound = 0
        number_list = remove_matching_digits(guess, self.randomNumber)
        guess_list = remove_matching_digits(self.randomNumber, guess)

        for index in range(4):
            digit = guess_list[index]
            if digit != " " and number_list.count(digit) > 0:
                digit_index = number_list.index(digit)
                number_list[digit_index] = " "
                self.bullsFound += 1

    def play(self):
        """
        Main method to play the game. This assumes that a random number has been assigned to the randomNumber field.
        :return:
        """
        while self.cowsFound < 4:
            raw_input = input("Enter a number :\n")
            formatted_guess = "{:0<4}".format(raw_input)

            self.count_cows(formatted_guess)
            self.count_bulls(formatted_guess)

            print(self.cowsFound, " cows, ", self.bullsFound, " bulls")

        print("\nCorrect !!!")


def remove_matching_digits(guess, number) -> list:
    """
    Convert the number into a list and replace any digit that matches a digit in the guess, at the same location, with a
     space.
    :param guess: to match against number
    :param number: to remove digits from
    :return: a 4 element list
    """
    number_list = list(number)
    for index in range(4):
        if number_list[index] == guess[index]:
            number_list[index] = " "
    return number_list


if __name__ == "__main__":
    # Generate a random number between 0 -> 9999 and convert it into a string 4 characters long
    rNumber = "{:0<4}".format(random.randint(1, 9999))

    game = CowsBullsGame(rNumber)
    game.play()
