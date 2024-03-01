def is_valid_path(gamestate, piece, colour, old_pos, new_pos):
    if piece == "r":
        if old_pos["row"] == new_pos["row"]:
            for i in range(old_pos["col"] - new_pos["col"]):
                if gamestate.board[old_pos["col"] + i][old_pos["row"]][1] == colour:
                    return False
            return True
    return True
