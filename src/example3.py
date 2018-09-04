#
# Decode a web page exercise
#
# Exercise from https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
#

import requests

from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"


def has_class(tag):
    """
    Does the supplied tag have a "class" attribute?
    :param tag: to check
    :return: True if class tag found
    """
    return tag.has_attr('class')


def print_all_classes(url):
    """
    Print to the screen all class tags in the given url
    :param url: of page to searh
    :return: Nothing
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="html.parser")
    all_class_tags = soup.find_all(has_class)

    all_classes= set()
    for found_tag in all_class_tags:
        tag_class_ = found_tag["class"]
        all_classes.update(tag_class_)

    for cls in all_classes:
        print("> ", cls)


def print_text_from_classes(url, *class_names):
    """
    Print to the screen all text in tags that have one of the supplied class attributes
    :param url: of page to scan
    :param class_names: list of class names used to filter the lines
    :return: Nothing
    """
    response = requests.get(url)

    soup = BeautifulSoup(response.text, features="html.parser")

    for story_body in soup.find_all(attrs={"class": class_names}):
        # print("##", story_body)
        if story_body.a:
            print(story_body.a.text.replace("\n", " ").strip())
        else:
            text = story_body.text
            print_wrapped_lines(text)


def print_wrapped_lines(text):
    """
    Print the text word wrapped to 80 ish columns, trying to break on a space.
    :param text: to print
    :return: Nothing
    """
    while len(text) > 80:
        # Search for a space between character 75-85
        index =75
        while index < 85 and index < len(text) and text[index] != " ":
            index = index+1
        print(text[0:index])
        if text[index] == " ":
            index = index +1
        text = text[index:]
    print(text)


if __name__ == "__main__":
    #
    # Print all of the class names in the page
    #
    # print_all_classes(base_url)
    #
    # or print the contents of the page
    #
    print_text_from_classes(base_url, "hed", "content-section", "dek")