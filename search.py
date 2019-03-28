import sys


def word_search():
    validate_input()


def validate_input():
    argument_count = len(sys.argv)
    if argument_count == 1:
        raise Exception("No argument was passed. Pass a path to word search text file as a string.")
    path = sys.argv[1]
    path_type = type(path)
    if type(path) != str:
        raise Exception("You passed an argument of type {}, this program only accepts strings."
                        .format(path_type))


def is_text_file(path):
    file_extension = path[-4:]
    if file_extension == ".txt":
        return True
    else:
        raise Exception(f'File was not a text file. Files should end in .txt."The file entered ended with '
                        f'{file_extension}.')


if __name__ == '__main__':
    word_search()
