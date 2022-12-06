from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    random_koala_fact()


def unique_koala_facts(n):
    i = 0
    list = []
    while n > i:
        list.append(random_koala_fact())
        n -= 1
        if n == 0:
            break
    return list


print(unique_koala_facts(3))


def num_joey_facts():
    initial_fact = random_koala_fact()  # call a fact before the loop
    times_seen_initial_fact = 0  # first counter
    num_joey_facts = 0  # second counter
    unique_facts = []
    while times_seen_initial_fact < 10:
        fact = random_koala_fact()  # call another fact in the loop
        if (
            fact == initial_fact
        ):  # c1 - compares the two called facts and adds to the first counter if they are identical
            times_seen_initial_fact += 1
        if (
            fact not in unique_facts
        ):  # c2 - checks if the second fact (wether identical to the first or not) is not in the list and adds it to it
            unique_facts.append(fact)
            if (
                "joey" in fact.lower()
            ):  # c3 - checks for the specified characteristic in a fact and adds to the second counter
                num_joey_facts += 1
    return num_joey_facts


print(num_joey_facts())


def koala_weight():
    initial_fact = random_koala_fact()
    counter = 0
    list = []
    weight_fact = ""
    while counter < 10:
        fact = random_koala_fact()
        if fact == initial_fact:
            counter += 1
        if fact not in list:
            if "kg" in fact:
                weight_fact = fact
    return f"{int(weight_fact[-5])}{int(weight_fact[-4])}kg"


print(koala_weight())
