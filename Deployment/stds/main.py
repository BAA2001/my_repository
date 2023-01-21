# Leave these lines untouched
__winc_id__ = "8c2e6882503c4baa9ce2e050497c3f2f"
__human_name__ = "stds"

import sys

# Your code here


def main():

    char_to_remove = sys.argv[1]
    text = sys.stdin.read()

    filtered_text = text.replace(char_to_remove, "")
    removed_count = text.count(char_to_remove)

    sys.stdout.write(filtered_text)
    sys.stderr.write(str(removed_count))

    # TODO: read text from stdin

    # TODO: Filter character given as an argument from the text

    # TODO: Print the result to stdout

    # TODO: Print the total number of removed characters to stderr
    ...


if __name__ == "__main__":
    main()
