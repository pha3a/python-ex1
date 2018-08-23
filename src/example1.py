
# Example exercise to form a list of ends from a given list
#
# See https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
#

def list_ends(originalList) -> list:
    if len(originalList) < 3:
        return originalList

    return list((originalList[0], originalList[len(originalList)-1]))

#
# Tests
#

x = ["a", "b", "c", "d"]

print(list_ends(x))

x = ["a", "d"]

print(list_ends(x))

x = ["a"]

print(list_ends(x))

x = []

print(list_ends(x))
