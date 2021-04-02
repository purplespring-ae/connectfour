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
        elif list_col(col, True).count(blank_spot) == 0:
            if verbose:
                print(f"Column {col} is full.")
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

    def list_col(icol, valid=False):
        if not valid:
            if not validate_col(icol):
                return False
        result = []
        for r in range(len(board)):
            result.append(board[r][icol])
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

    def check_win(check_r, check_c):
        '''
        ? only check the most recently added spot, as there can't be a win from
        the start and no spots can move.

        once game is fully running: allow AI to see three-in-a-rows and block them, as first stage
        of a rudimentary computer player
        '''
        possible_directions = {
            "NW": {"delta_r": -1, "delta_c": -1, "opp": "SE"},
            "N": {"delta_r": -1, "delta_c": 0, "opp": "S"},
            "NE": {"delta_r": -1, "delta_c": +1, "opp": "SW"},
            "E": {"delta_r": 0, "delta_c": +1, "opp": "W"},
            "SE": {"delta_r": +1, "delta_c": +1, "opp": "NW"},
            "S": {"delta_r": +1, "delta_c": 0, "opp": "N"},
            "SW": {"delta_r": +1, "delta_c": -1, "opp": "NE"},
            "W": {"delta_r": 0, "delta_c": +1, "opp": "E"},
        }
        checked_directions = []

        def check_direction(from_r, from_c, dir_):
            # set up vector and choose first target
            delta_r = possible_directions[dir_]["delta_r"]
            delta_c = possible_directions[dir_]["delta_c"]
            target_r, target_c = from_r + delta_r, check_c + delta_c
            # loop-breaking vars
            match_val = board[from_r][from_c]
            dir_exhausted = False
            num_connect = 0

            while not dir_exhausted and num_connect < 3:
                if not validate_row(target_r) \
                        or not validate_col(target_c) \
                        or not board[target_r][target_c] == match_val:
                    # print(f"{from_r},{from_c} has no matches to the {dir}."")
                    dir_exhausted = True
                    break
                else:
                    print(
                        f"{target_r},{target_c} is a connect to the {dir_} for {from_r},{from_c}.")
                    num_connect += 1
                    # adjust position to continue in that direction
                    target_r, target_c = target_r + delta_r, target_c + delta_c
            return num_connect

        for dir, vals in possible_directions.items():
            if dir in checked_directions:
                continue
            opp_dir = possible_directions[dir]["opp"]
            dir_match = check_direction(check_r, check_c, dir)
            checked_directions.append(dir)
            opp_match = check_direction(check_r, check_c, opp_dir)
            checked_directions.append(opp_dir)
            if dir_match + opp_match >= 3:
                print(
                    "SOMEONE WON THE GAME I DON'T KNOW WHO YET OR WHAT TO DO ABOUT IT THOUGH")
                break
            else:
                pass

    blank_spot = " . "
    players = [" X ", " O "]
    current_player = 0
    board = construct_board(r=6, c=7, blank_spot=blank_spot)
    draw_board(board)

    # # TEST MOVES
    # make_move(5, current_player)
    # current_player = toggle_player(current_player)
    # make_move(2, current_player)
    # current_player = toggle_player(current_player)
    # make_move(5, current_player)
    # current_player = toggle_player(current_player)
    # make_move(3, current_player)
    # current_player = toggle_player(current_player)
    # make_move(5, current_player)
    # current_player = toggle_player(current_player)
    # make_move(2, current_player)
    # current_player = toggle_player(current_player)
    # make_move(5, current_player)
    # current_player = toggle_player(current_player)
    # make_move(2, current_player)
    # current_player = toggle_player(current_player)
    # check_win(4, 5)


if __name__ == "__main__":
    play_game()
