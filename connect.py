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
        if col > len(board[0])-1 or col < 0:
            if verbose:
                print(f"Column {col} doesn't exist on the board.")
            return False
        else:
            return True

    def validate_row(row, verbose=False):
        if row > len(board)-1 or row < 0:
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

    def toggle_player(last_player):
        new_player = 1 - last_player
        print(f"It's {players[new_player]}'s turn.")
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

    def get_neighbours_matching(irow, icol):
        # currently not used for anything - possibly useful for check_win?
        result = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                this_spot = board[r][c]
                if this_spot in players:
                    neighbours = get_neighbours(r, c)
                    for n in neighbours:
                        checkr, checkc = n[0], n[1]
                        checkval = board[checkr][checkc]
                        if this_spot == checkval:
                            print(
                                f"Matching neighbour for {checkval} found at ({checkr},{checkc}).")
                            result.append((checkr, checkc))

    def check_win():
        '''
        to cut down on needless checking, once a matching neighbour is found,
        continue checking in that direction until it's not a match
        Start with possible_directions = eg ["nw", "n", "ne", "w", "e", "sw", "s", "se"]
        eliminate directions in turn

        ? only check the most recently added spot, as there can't be a win from
        the start and no spots can move.

        once game is fully running: allow AI to see three-in-a-rows and block them. first stage
        of a rudimentary computer player
        '''
        possible_directions = {
            "nw": {"delta_r": -1, "delta_c": -1, "rmax": , "cmax": , "matches": []},
            "n": {"delta_r": -1, "delta_c": 0, "rmax": , "cmax":  "matches": []},
            "ne": {"delta_r": -1, "delta_c": +1, "rmax": , "cmax":  "matches": []},
            "e": {"delta_r": 0, "delta_c": +1, "rmax":, "cmax":  "matches": []},
            "se": {"delta_r": +1, "delta_c": +1, "rmax":, "cmax":  "matches": []},
            "s": {"delta_r": +1, "delta_c": 0, "rmax": , "cmax":  "matches": []},
            "sw": {"delta_r": +1, "delta_c": -1, "rmax": , "cmax":  "matches": []},
            "w": {"delta_r": 0, "delta_c": +1, "rmax": , "cmax":  "matches": []},
        }

    blank_spot = " . "
    players = [" X ", " O "]
    current_player = 0
    board = construct_board(r=6, c=7, blank_spot=blank_spot)
    draw_board(board)

    make_move(5, current_player)
    current_player = toggle_player(current_player)
    make_move(2, current_player)
    current_player = toggle_player(current_player)
    make_move(5, current_player)
    current_player = toggle_player(current_player)
    make_move(3, current_player)
    current_player = toggle_player(current_player)
    check_win()


if __name__ == "__main__":
    play_game()
