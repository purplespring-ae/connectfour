import itertools


def play_game():

    def construct_board(r, c, blank_spot):
        board = []
        # create rows
        for i in range(r):
            row = []
            for n in range(c):
                row.append(blank_spot)
            board.append(row)
        return(board)

    def draw_board(board):
        h_separator = " - " * 13
        v_separator = " | "
        print("")
        # iterate over rows
        for r in range(len(board)):
            row_str = ""
            # iterate over columns using col 1 to set range
            for c in range(len(board[0])):
                row_str += board[r][c]
                row_str += v_separator
            # remove trailing v_separator
            row_str = row_str[:-2]
            print(row_str)
            # prevent trailing h_separator
            if not r == len(board)-1:
                print(h_separator)

    def validate_col(col):
        if col > len(board[0]) or col < 0:
            print("That column doesn't exist on the board.")
            return False
        else:
            return True

    def list_col(icol):
        if not validate_col(icol):
            return False
        result = []
        for r in range(len(board)):
            result.append(board[r][icol])
        # print(result)
        return(result)

    def col_floor(icol):
        col = list_col(icol)
        for r in range(len(col)):
            if col[r] in players:
                return r-1
        return len(col)-1

    def make_move(icol, player):
        if not validate_col(icol):
            return False
        irow = col_floor(icol)
        board[irow][icol] = players[player]
        draw_board(board)

    def say_player():
        print(f"It's {players[current_player]}'s turn.")

    def toggle_player(last_player):
        new_player = 1 - last_player
        return new_player

    blank_spot = " . "
    players = [" X ", " O "]
    current_player = 0
    board = construct_board(r=6, c=7, blank_spot=blank_spot)
    draw_board(board)

    # print(col_floor(2))
    make_move(2, current_player)
    current_player = toggle_player(current_player)
    say_player()
    make_move(2, current_player)
    current_player = toggle_player(current_player)
    say_player()
    # print(col_floor(2))


if __name__ == "__main__":
    play_game()
