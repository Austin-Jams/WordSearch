import sys


def word_search():
    validate_input()


def validate_input():
    argument_count = len(sys.argv)
    if argument_count == 1:
        raise Exception("No argument was passed. Pass a path to word search text file as a string.")


if __name__ == '__main__':
    word_search()