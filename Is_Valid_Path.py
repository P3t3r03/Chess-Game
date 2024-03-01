def is_valid_path_pawn(gamestate, piece, colour, old_pos, new_pos):
    if colour == "l":
        if old_pos["row"] == 6 and new_pos["row"] == 4 and (gamestate.board[new_pos["col"]][4] == "  " and  # double move off of start
                                                            gamestate.board[new_pos["col"]][5] == "  " and
                                                            old_pos["col"] == new_pos["col"]):
            return True
        elif old_pos["col"] == new_pos["col"] and old_pos["row"] == new_pos["row"] + 1 and gamestate.board[new_pos["col"]][new_pos["row"]] == "  ":
            return True
        elif old_pos["row"] == new_pos["row"] + 1 and abs(old_pos["col"] - new_pos["col"]) == 1 and gamestate.board[new_pos["col"]][new_pos["row"]][1] == "d": # Checks for takable pieces
            return True
        return False
    elif colour == "d":
        if old_pos["row"] == 1 and new_pos["row"] == 3 and (gamestate.board[new_pos["col"]][2] == "  " and  # double move off of start
                                                            gamestate.board[new_pos["col"]][3] == "  " and
                                                            old_pos["col"] == new_pos["col"]):
            return True
        elif old_pos["col"] == new_pos["col"] and old_pos["row"] == new_pos["row"] - 1 and gamestate.board[new_pos["col"]][new_pos["row"]] == "  ":
            return True
        elif old_pos["row"] == new_pos["row"] - 1 and abs(old_pos["col"] - new_pos["col"]) == 1 and gamestate.board[new_pos["col"]][new_pos["row"]][1] == "l": # Checks for takable pieces
            return True
        return False





def is_valid_path_rook(gamestate, piece, colour, old_pos, new_pos):
    if old_pos["row"] == new_pos["row"]:
        if old_pos["col"] > new_pos["col"]:
            start = new_pos["col"] + 1
            end = old_pos["col"]
        else:
            start = old_pos["col"] + 1
            end = new_pos["col"]
        for i in range(start, end):
            if gamestate.board[i][old_pos["row"]] != "  ":
                return False
        if gamestate.board[new_pos["col"]][new_pos["row"]][1] == colour:
            return False
        return True
    elif old_pos["col"] == new_pos["col"]:
        if old_pos["row"] > new_pos["row"]:
            start = new_pos["row"] + 1
            end = old_pos["row"]
        else:
            start = old_pos["row"] + 1
            end = new_pos["row"]
        for i in range(start, end):
            if gamestate.board[old_pos["col"]][i] != "  ":
                return False
        if gamestate.board[old_pos["col"]][new_pos["row"]][1] == colour:
            return False
        return True


def is_valid_path_bishop(gamestate, piece, colour, old_pos, new_pos):
    delta_row = 1 if new_pos["row"] > old_pos["row"] else -1
    delta_col = 1 if new_pos["col"] > old_pos["col"] else -1
    row = old_pos["row"] + delta_row
    col = old_pos["col"] + delta_col
    while row != new_pos["row"] and col != new_pos["col"]:
        if gamestate.board[col][row] != "  ":
            return False
        row += delta_row
        col += delta_col
    if gamestate.board[new_pos["col"]][new_pos["row"]][1] == colour:
        return False
    return True

def is_valid_path_queen(gamestate, piece, colour, old_pos, new_pos):
    if old_pos["row"] == new_pos["row"]:
        return is_valid_path_rook(gamestate, piece, colour, old_pos, new_pos)
    elif old_pos["col"] == new_pos["col"]:
        return is_valid_path_rook(gamestate, piece, colour, old_pos, new_pos)
    elif abs(old_pos["row"] - new_pos["row"]) == abs(old_pos["col"] - new_pos["col"]):
        return is_valid_path_bishop(gamestate, piece, colour, old_pos, new_pos)
    return False