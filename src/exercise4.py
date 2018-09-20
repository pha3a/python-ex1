# Example exercise to dictionary of birthdays from a json file.
#
# See https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
#
import json
from collections import Counter


class Birthdays:

    month_name = ("Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

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

    def count_months(self):
        """
        Count the number of people born in each month and print the result as a dictionary. The key being the
        month name rather than the month number.
        :return: Nothing
        """
        print(">>> Number of people born in each month is:")
        months = list()
        for date in self.birthday_dictionary.values():
            month = date.split("/")[1]
            months += month
        counter = dict(Counter(months))
        result = dict()
        keys = counter.keys()
        sorted_keys = sorted(keys)
        for month_number in sorted_keys:
            name = self.month_name[int(month_number)-1]
            result[name] = counter[month_number]

        print(result)

    def execute(self, action):
        """
        Dispatcher method
        """
        methods = {
            "p": "show_all_names",
            "l": "show_single_birthday",
            "a": "add_new_birthday",
            "m": "count_months"
        }
        method_name = methods.get(action)
        if method_name:
            method = getattr(self, method_name)
            method()
        else:
            print("Unknown action '", action, "'")


if __name__ == "__main__":

    birthdays = Birthdays()

    action = "p"
    print(">>> Welcome to birthday dictionary.")
    while action != "x":
        action = input(">>> What do you want to do (a=add, p=print list, l=look up, m=count months, x=exit)? ")
        birthdays.execute(action)
