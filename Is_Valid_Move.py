def is_valid_move(gamestate, piece, new_pos, old_pos):
    piece_colour = piece[1]
    piece_type = piece[0]
    if gamestate.board[old_pos["col"]][old_pos["row"]] == piece:
        if piece_type == "p" and old_pos["col"] == new_pos["col"]:
            if piece_colour == "l" and (old_pos["row"] == new_pos["row"] + 1 or (old_pos["row"] == 6 and new_pos["row"] == 4)):
                return True
            elif piece_colour == "d" and (old_pos["row"] == new_pos["row"] - 1 or (old_pos["row"] == 1 and new_pos["row"] == 3)):
                return True
        elif piece_type == "r" and (old_pos["col"] == new_pos["col"] or old_pos["row"] == new_pos["row"]):
            return True
        elif piece_type == "b" and abs(old_pos["col"] - new_pos["col"]) == abs(old_pos["row"] - new_pos["row"]):
            return True
        elif piece_type == "q" and ((old_pos["col"] == new_pos["col"] or old_pos["row"] == new_pos["row"]) or
                                    abs(old_pos["col"] - new_pos["col"]) == abs(old_pos["row"] - new_pos["row"])):
            return True
        elif piece_type == "k" and (abs(old_pos["col"] - new_pos["col"]) <= 1) and (abs(old_pos["row"] - new_pos["row"]) <= 1):
            return True
        elif piece_type == "n" and (
                (abs(old_pos["col"] - new_pos["col"]) == 2 and abs(old_pos["row"] - new_pos["row"]) == 1) or
                (abs(old_pos["col"] - new_pos["col"]) == 1 and abs(old_pos["row"] - new_pos["row"]) == 2)):
            return True

        return False
    return False
