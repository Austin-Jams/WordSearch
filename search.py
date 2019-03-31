import sys
import os

def word_search():
    opened_file = validate_input_file()
    if not validate_input_content(opened_file):
        raise Exception("Content of file does not meet input criteria.")


def validate_input_content(opened_file):
    key_words_string = opened_file.readline()
    if not validate_key_words(key_words_string):
        return False
    return True


def validate_key_words(key_words_string):
    words = key_words_string.split(",")
    for word in words:
        if len(word) <= 1 or not word.isalpha():
            print("Words must only contain members of the alphabet and must be longer than one letter.")
            return False
    return True


def validate_input_file():
    argument_count = len(sys.argv)
    if argument_count == 1:
        raise Exception("No argument was passed. Pass a path to word search text file as a string.")
    path = sys.argv[1]
    path_type = type(path)
    if type(path) != str:
        raise Exception("You passed an argument of type {}, this program only accepts strings."
                        .format(path_type))
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(dir_path, path)
        opened_file = open(file)
        return opened_file
    except FileNotFoundError:
        print("File not found at path")


def is_text_file(path):
    file_extension = path[-4:]
    if file_extension == ".txt":
        return True
    else:
        raise Exception(f'File was not a text file. Files should end in .txt."The file entered ended with '
                        f'{file_extension}.')


if __name__ == '__main__':
    word_search()
