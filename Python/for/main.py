from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

# List with the shortest country names


def shortest_names(list):
    cwsn = []
    for element in list:
        if len(element) < 5:
            cwsn.append(element)
    print(cwsn)


shortest_names(get_countries())

# List with countries that have the most vowels


def most_vowels(list):
    vowels = "aeiou"  # define vowels
    top_list = (
        []
    )  # create a new list for storing words from the original list that have the most vowels
    for element in list:  # for every element/word in list v
        vowel_counter = 0  # we make a variable that counts the vowels of a word
        for el in element:  # for every element/letter of word of list v
            if (
                el in vowels
            ):  # condition: if letter of word of list is in the list vowels v
                vowel_counter += 1  # we add one to the vowel counter v
                top_list.append(
                    (element, vowel_counter)
                )  # and we append word to the top list along with its vouwel count
    sorted_list = sorted(
        top_list, key=lambda t: t[1], reverse=True
    )  #! create a new list that sorts the previous new list
    print(sorted_list[0], sorted_list[1], sorted_list[2])


most_vowels(get_countries())


def alphabet_set(list):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    new_list = []
    for element in list:
        for el in element:
            if el in alphabet and el not in new_list:
                if element not in new_list:
                    new_list.append(element)
                alphabet.remove(el)

    print(new_list)


alphabet_set(get_countries())
