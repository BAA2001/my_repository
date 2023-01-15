# Do not modify these lines
import os

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Test your functions here to make sure the functionality remains the same.
def main():
    foo = list(range(10))
    print(
        get_item_from_list(foo, 9),
        get_item_from_list(foo, -1),
        get_item_from_list(foo, 10),
    )
    ...


"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""


# Returns the addition of x and y if it's defined, otherwise returns 0
def add(x=0, y=0):
    try:
        print(x + y)
    except TypeError:
        print("you cannot multiply a string with int or float!")


add("poop", 2.1)

# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist
def read_file(filename):
    try:
        if os.path.exists(filename):
            return open(filename, "r").read()
    except FileNotFoundError:
        print("")


read_file("poop.txt")


# Returns item at `index` from list `l` if possible, otherwise returns None
def get_item_from_list(l, index):
    try:
        max_index = len(l) - 1
        min_index = -1 - max_index
        if index <= max_index and index >= min_index:
            return l[index]
    except TypeError:
        print("no '<=' between instances of 'str' and 'int'")


get_item_from_list("list", "index")

if __name__ == "__main__":
    main()
