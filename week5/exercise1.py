# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.
Your job is to go through it and make it as good as you can.
That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.
The resulting file should feel as close to english as possible.
It must also pass the linter.
This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.
Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function


# return a lit of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Docstring."""
    reverse = False
    if stop > start:
        reverse = True
    count = start
    listed = []
    while count not in (stop, -1):
        line = message + " {}".format(count)
        listed.append(line)
        if reverse is True:
            count += 1
        else:
            count -= 1
    listed.append(completion_message)
    return listed


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Docstring."""
    hypo = (base**2 + height**2)**(0.5)
    return hypo


def calculate_area(base, height):
    """Docstring."""
    area = base*height*0.5
    return area


def calculate_perimeter(base, height):
    """Docstring."""
    side = calculate_hypotenuse(height, base)
    perim = side + base + height
    return perim
    pass


def calculate_aspect(base, height):
    """Docstring."""
    if height > base:
        return "tall"
    elif height == base:
        return "equal"
    else:
        return "wide"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Docstring."""
    return {"area": calculate_area(base, height),
            "perimeter": calculate_perimeter(base, height),
            "height": height,
            "base": base,
            "hypotenuse": calculate_hypotenuse(base, height),
            "aspect": calculate_aspect(base, height),
            "units": units}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Docstring."""
    tall = """
            {height}
            |
            |     |\\
            |____>| \\ {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)

    if facts_dictionary.get('aspect') == "tall":
        aspect = tall
    elif facts_dictionary.get('aspect') == "wide":
        aspect = wide
    else:
        aspect = equal

    returned = aspect.format(**facts_dictionary)
    returned = returned + "\n" + facts
    return returned


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Docstring."""
    a_dictionary = get_triangle_facts(base, height, "mm")
    b_dictionary = {"facts": a_dictionary}
    diagram = tell_me_about_this_right_triangle(a_dictionary)

    if return_diagram and return_dictionary:
        return ({"diagram": diagram, "facts": a_dictionary})
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return b_dictionary
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Docstring."""
    list1 = list_of_words_with_lengths(range(3, 21, 2))
    list2 = list_of_words_with_lengths(range(20, 3, -2))
    listed = list1 + list2
    return listed


def get_a_word_of_length_n(length):
    """Docstring."""
    try:
        length = int(length)
        if length > 0:
            import requests
            baseURL = "http://www.setgetgo.com/randomword/get.php?len="
            url = baseURL + str(length)
            r = requests.get(url)
            message = r.text
            return message
    except Exception:
        pass


def list_of_words_with_lengths(list_of_lengths):
    """Docstring."""
    listed = []
    for i in list_of_lengths:
        listed.append(get_a_word_of_length_n(i))
    return listed


if __name__ == "__main__":
    pass
