def is_valid_move(gamestate, piece, new_pos, old_pos):
    if gamestate.board[old_pos["col"]][old_pos["row"]] == piece:
        if new_pos["col"] == old_pos["col"]:
            return True
        return False
    return False
