import parmap


def create_processes(key_word_list,board):
    results = parmap.map(solve,key_word_list,board, pm_processes=len(key_word_list))
    return print("Done")



def solve(word,board):
    return 1


def search_right(current_position,board,word,forward):


def search_up(current_position,board,forward):


def search_down(current_position,board,forward):


def search_left(current_position,board,forward):


def search_up_right(current_position,board,forward):


def search_down_right(current_position,board,forward):


def search_down_left(current_position,board,forward):


def search_up_left(current_position,board,forward):