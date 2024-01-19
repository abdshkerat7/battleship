import helper
from helper import *



Msg_for_location = 'enter cordinate'
MSG_ERROR = "input is not good"
msg_to_player = 'enter another location'

def init_board(rows, columns):
    lst = [[helper.WATER for i in range(columns)] for j in range(rows)]
    return lst


def cell_loc(name):
    y = int(ord(name[0]))
    if y >= ord('A') and y <= ord('Z'):
        y -= 65
    if y >= ord('a') and y <= ord('z'):
        y -= 97
    x = int(name[1:len(name)]) - 1
    return (x, y)


def valid_ship(board, size, loc):
    if loc[0] + size > len(board):
        return False
    for i in range(size):
        if board[loc[0] + i][loc[1]] != helper.WATER:
            return False
    return True


def add_to_player_board(board, loc, size):
    x = loc[0]
    y = loc[1]
    for i in range(size):
        board[x + i][y] = helper.SHIP
    return board



def create_player_board(rows, columns, ship_sizes):
    player_board = init_board(rows, columns)
    if len(ship_sizes) == 0:
        return player_board
    i = 0
    user_input = helper.get_input(Msg_for_location)
    while i < len(ship_sizes):
        loc = cell_loc(user_input)
        flag = valid_ship(player_board, ship_sizes[i], loc)
        if flag:
            player_board = add_to_player_board(player_board, loc, ship_sizes[i])
            i += 1
            if i != len(ship_sizes):
                helper.print_board(player_board)
            if i < len(ship_sizes):
                user_input = helper.get_input(Msg_for_location)
        else:
            helper.print_board(player_board)
            user_input = helper.get_input(MSG_ERROR)
    return player_board

def get_cells(rows, cols):
    cells = []
    for i in range(rows):
        for j in range(cols):
            x = (i, j)
            cells.append(x)
    return cells


def creat_computer_board(rows, cols, ship_sizes):
    location = [(0,0), (0,1), (0,2)]
    computer_board = init_board(rows, cols)
    # cells = get_cells(rows, cols) #T=============================================================
    if len(ship_sizes) == 0:
        return computer_board
    i = 0
    while i < len(ship_sizes):
        if i < len(ship_sizes) + 1:
            print(("S", computer_board, ship_sizes[i], location))
        # loc = helper.choose_ship_location(computer_board, ship_sizes[i], location)
        loc = location[0]
        location = location[1:]
        flag = valid_ship(computer_board, ship_sizes[i], loc)
        if flag:
            computer_board = add_to_player_board(computer_board, loc, ship_sizes[i])
            i+=1

    return computer_board


def fire_torpedo(board, loc):
    row = loc[0]
    col = loc[1]
    if row >= len(board) or col >= len(board[0]):
        return board
    if board[row][col] == helper.WATER:
        board[row][col] =helper.HIT_WATER
        return board
    if board[row][col] == helper.SHIP:
        board[row][col] = helper.HIT_SHIP
        return board


def check_end_of_the_game(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == helper.SHIP:
                return False
    return True

def check_input(computer_water, cells):
    input_from_player = helper.get_input(msg_to_player)
    print(("T", computer_water, cells))

    while True:
        # we will check if the loc have "XN"
        loc = cell_loc(input_from_player)
        row = loc[0]
        col = loc[1]
        if row >= len(computer_water) or col >= len(computer_water[0]):
            input_from_player = helper.get_input("not good cor")
        elif computer_water[row][col] == helper.HIT_WATER or computer_water[row][col] == HIT_SHIP:
            input_from_player = helper.get_input("you hit it before")
        else:
            break
    return loc

def ask_user_if_play_again(name):
    if name == 'Y':
        return False
    if name == 'N':
        return False
    return True


def check_if_user_want_to_play():
    ask_if_play_again = helper.get_input("if you want to play again choose : Y else choose: N")
    while ask_user_if_play_again(ask_if_play_again):
        ask_if_play_again = helper.get_input("please choose : Y else choose: N")
    return ask_if_play_again


def play():
    cells = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
    computer_water = init_board(helper.NUM_ROWS, helper.NUM_COLUMNS)

    helper.print_board(computer_water)
    player_board = create_player_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)

    computer_board = creat_computer_board(helper.NUM_ROWS, helper.NUM_COLUMNS, helper.SHIP_SIZES)

    helper.print_board(player_board, computer_water)
    flag = True
    while flag:
        hit_loc = check_input(computer_water, cells)
        # computer_hit_loc = helper.choose_torpedo_target(computer_board, cells)
        computer_hit_loc = cells[0]
        cells = cells[1:]



        if computer_board[hit_loc[0]][hit_loc[1]] == helper.WATER:
            computer_board[hit_loc[0]][hit_loc[1]] = helper.HIT_WATER
            computer_water[hit_loc[0]][hit_loc[1]] = helper.HIT_WATER

        if computer_board[hit_loc[0]][hit_loc[1]] == helper.SHIP:
            computer_board[hit_loc[0]][hit_loc[1]] = helper.HIT_SHIP
            computer_water[hit_loc[0]][hit_loc[1]] = helper.HIT_SHIP

        if player_board[computer_hit_loc[0]][computer_hit_loc[1]] == helper.WATER:
            player_board[computer_hit_loc[0]][computer_hit_loc[1]] = helper.HIT_WATER

        if player_board[computer_hit_loc[0]][computer_hit_loc[1]] == helper.SHIP:
            player_board[computer_hit_loc[0]][computer_hit_loc[1]] = helper.HIT_SHIP

        if check_end_of_the_game(computer_board):
            helper.print_board(player_board, computer_water)
            return





        if check_end_of_the_game(computer_board):
            helper.print_board(player_board, computer_water)
            return
        helper.print_board(player_board, computer_water)


def main():
    flag = True
    while flag:
        play()
        ask = check_if_user_want_to_play()
        if ask == "N":
            flag = False




if __name__ == "__main__":
    main()
