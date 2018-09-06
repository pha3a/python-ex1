# Example exercise to dictionary of birthdays from a json file.
#
# See https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
#
import json


class Birthdays:

    def __init__(self):
        with open('birthdays.json', 'r') as infile:
            self.birthday_dictionary = json.load(infile)

    def show_all_names(self):
        print(">>> We know about:")

        for name in self.birthday_dictionary.keys():
            print(name)

    def show_single_birthday(self):
        request = input(">>> Whos birthday do you want?\n")

        print(self.birthday_dictionary[request])

    def add_new_birthday(self):
        name = input(">>> Enter name :")
        birthday = input(">>> Enter birthday ")

        self.birthday_dictionary[name] = birthday

        with open('birthdays.json', 'w') as outfile:
            json.dump(self.birthday_dictionary, outfile)


if __name__ == "__main__":

    birthdays = Birthdays()

    action = "p"
    print(">>> Welcome to birthday dictionary.")
    while action != "x":
        action = input(">>> What do you want to do (a=add, p=print list, l=look up, x=exit)? ")
        if action == "p":
            birthdays.show_all_names()
        elif action == "l":
            birthdays.show_single_birthday()
        elif action == "a":
            birthdays.add_new_birthday()
