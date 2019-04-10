import parmap


def create_processes(key_word_list,board):
    results = parmap.map(solve,key_word_list,board, pm_processes=len(key_word_list))
    return print("Done")


def solve(word,board):
    return 1


def search_right(current_position, board, word, forward):
    if not forward:
        word = word[::-1]
    string_check = ''
    row = current_position[0]
    column = current_position[1]
    while word.startswith(string_check):
        if string_check == word:
            return True
        string_check += board[row][column]
        column += 1


def search_down(current_position, board, word, forward):
    if not forward:
        word = word[::-1]
    string_check = ''
    row = current_position[0]
    column = current_position[1]
    while word.startswith(string_check):
        if string_check == word:
            return True
        string_check += board[row][column]
        row += 1


def search_down_right(current_position, board, word, forward):
    if not forward:
        word = word[::-1]
    string_check = ''
    row = current_position[0]
    column = current_position[1]
    while word.startswith(string_check):
        if string_check == word:
            return True
        string_check += board[row][column]
        row += 1
        column += 1


def search_down_left(current_position, board, word, forward):
    if not forward:
        word = word[::-1]
    string_check = ''
    row = current_position[0]
    column = current_position[1]
    while word.startswith(string_check):
        if string_check == word:
            return True
        string_check += board[row][column]
        row += 1
        column -= 1






