# Example exercise to dictionary of birthdays from a json file.
#
# See https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
#
import json
from collections import Counter
from bokeh.plotting import figure, output_file, show


class Birthdays:
    available_actions = {
        "n": "show_all_names",
        "l": "lookup_birthday",
        "a": "add_new_birthday",
        "t": "total_months",
        "g": "graph_months"
    }

    month_name = ("Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec")

    def __init__(self):
        with open('birthdays.json', 'r') as infile:
            self.birthday_dictionary = json.load(infile)

    def show_all_names(self):
        print(">>> We know about:")

        for name in self.birthday_dictionary.keys():
            print(name)

    def lookup_birthday(self):
        request = input(">>> Whos birthday do you want?\n")

        if request in self.birthday_dictionary:
            print(self.birthday_dictionary[request])
        else:
            print(">>> I don't know that person")

    def add_new_birthday(self):
        name = input(">>> Enter name :")
        birthday = input(">>> Enter birthday ")

        self.birthday_dictionary[name] = birthday

        with open('birthdays.json', 'w') as outfile:
            json.dump(self.birthday_dictionary, outfile)

    def total_months(self):
        """
        Count the number of people born in each month and print the result as a dictionary. The key being the
        month name rather than the month number.
        :return: Nothing
        """
        print(">>> Number of people born in each month is:")
        counter = self.count_months()
        result = dict()
        keys = counter.keys()
        sorted_keys = sorted(keys)
        for month_number in sorted_keys:
            name = self.month_name[int(month_number) - 1]
            result[name] = counter[month_number]
        print(result)

    def count_months(self):
        """
        Count the number of birthdays in each month.
        :return: a dictionary of month -> total
        """
        months = list()
        for date in self.birthday_dictionary.values():
            month = date.split("/")[1]
            months.append(month)
        counter = dict(Counter(months))
        return counter

    def graph_months(self):
        """
        Display a graph of months with a count of the number of birthdays in that month
        :return: Nothing
        """
        months = self.count_months()
        keys = months.keys()
        sorted_keys = sorted(keys)
        month_names = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
        # x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for month_number in sorted_keys:
            y[int(month_number) - 1] = int(months[month_number])

        # output to static HTML file
        output_file("plot.html")

        # create a new plot with a title and axis labels
        p = figure(title="Birthdays in each month", x_axis_label='Month',
                   y_axis_label='No. people with a birthday in month',
                   x_range=month_names, toolbar_location=None, tools="",
                   plot_height=350)
        p.vbar(x=month_names, top=y, width=0.75)
        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        show(p)

    def display_available_actions(self):
        for available_action in self.available_actions.keys():
            print(available_action, "->", self.available_actions.get(available_action))


def execute(selected_action, birthdays):
    """
       Dispatcher method
       """
    method_name = birthdays.available_actions.get(selected_action)
    if method_name:
        method = getattr(birthdays, method_name)
        method()
    else:
        print("Unknown action '", selected_action, "'")


def prompt_user(birthdays):
    print("\nActions:")
    birthdays.display_available_actions()
    print("x -> EXIT")
    return input(">>> What do you want to do?")


if __name__ == "__main__":

    dictionary = Birthdays()

    print(">>> Welcome to birthday dictionary.")
    action = prompt_user(dictionary)

    while action != "x":
        execute(action, dictionary)
        action = prompt_user(dictionary)
