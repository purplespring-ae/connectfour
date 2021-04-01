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

    def validate_col(col, verbose=False):
        if col > len(board[0]) or col < 0:
            if verbose:
                print(f"Column {col} doesn't exist on the board.")
            return False
        else:
            return True

    def validate_row(row, verbose=False):
        if row > len(board) or row < 0:
            if verbose:
                print(f"Row {row} doesn't exist on the board.")
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

    def get_neighbours(irow, icol):
        result = []
        # try 3x3 square including (irow-1, icol-1) to (irow+1, icol+1) excluding self
        for r in range(irow-1, irow+2):
            if validate_row(r):
                for c in range(icol-1, icol+2):
                    if validate_col(c) and not (icol == c and irow == r):
                        result.append((r, c))
        return result

    def check_win():
        def check_row():
            for r in range(len(board)):
                for c in range(len(board[r])):
                    # print(f"Checking {r}, {c}")
                    this_spot = board[r][c]
                    print(this_spot)
                    neighbours = get_neighbours(r, c)

        def check_col():
            pass

        def check_diag_r():
            pass

        def check_diag_l():
            pass

        check_row()

    blank_spot = " . "
    players = [" X ", " O "]
    current_player = 0
    board = construct_board(r=6, c=7, blank_spot=blank_spot)
    draw_board(board)

    check_win()
    # make_move(2, current_player)
    # current_player = toggle_player(current_player)
    # say_player()
    # make_move(2, current_player)
    # current_player = toggle_player(current_player)
    # say_player()


if __name__ == "__main__":
    play_game()
