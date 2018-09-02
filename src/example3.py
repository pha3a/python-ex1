
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
            print(story_body.text)


if __name__ == "__main__":
    #
    # Print all of the class names in the page
    #
    # print_all_classes(base_url)
    #
    # or print the contents of the page
    #
    print_text_from_classes(base_url, "hed", "rubric", "dek")