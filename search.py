import sys
import os
from solve import solve, create_processes


def word_search():
    opened_file = validate_input_file()
    if not validate_input_content(opened_file):
        print("Content not valid")
        exit()
    opened_file.seek(0)
    key_word_list = opened_file.readline().rstrip("\n").split(",")
    board = create_board(opened_file)
    opened_file.close()
    create_processes(key_word_list,board)



def validate_input_content(opened_file):
    if opened_file is None:
        print("File not open.")
        return False
    key_words_string = opened_file.readline()
    if not validate_key_words(key_words_string):
        return False
    if not validate_board(opened_file):
        return False
    return True


def create_board(opened_file):
    opened_file.seek(0)
    board = [row.rstrip('\n').split(',') for row in opened_file]
    board.pop(0)
    return board


def validate_board(opened_file):
    board = create_board(opened_file)
    total_letters_processed = 0
    row_count = 0
    for row in board:
        row_length = len(row)
        row_count += 1
        i = 0
        while i < row_length:
            total_letters_processed += 1
            if len(row[i]) is not 1:
                print("Not properly comma separated.")
                return False
            elif not row[i].isalpha():
                print("Input must be apart of the alphabet.")
                return False
            elif i == row_length:
                if (total_letters_processed/row_count) is not row_length:
                    print("Not a consistent row length.")
                    return False
            i += 1
    if (total_letters_processed%row_count is not 0) and (int((total_letters_processed/row_count)) is not row_count):
        print("Not a square.")
        return False
    return True


def validate_key_words(key_words_string):
    key_words_string = key_words_string.rstrip("\n")
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
        exit()


def is_text_file(path):
    file_extension = path[-4:]
    if file_extension == ".txt":
        return True
    else:
        raise Exception(f'File was not a text file. Files should end in .txt."The file entered ended with '
                        f'{file_extension}.')


if __name__ == '__main__':
    sys.argv.append("Tests\TestData\goodData1.txt")
    word_search()
