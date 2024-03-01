from Is_Valid_Path import *

def is_valid_move(gamestate, piece, new_pos, old_pos):
    piece_colour = piece[1]
    piece_type = piece[0]
    if new_pos == old_pos:
        return False
    if gamestate.board[old_pos["col"]][old_pos["row"]] == piece and old_pos != new_pos:
        if piece_type == "p":
            return is_valid_path_pawn(gamestate, piece_type, piece_colour, old_pos, new_pos)
        elif piece_type == "r" and (old_pos["col"] == new_pos["col"] or old_pos["row"] == new_pos["row"]):
            return is_valid_path_rook(gamestate, piece_type, piece_colour, old_pos, new_pos)
        elif piece_type == "b" and abs(old_pos["col"] - new_pos["col"]) == abs(old_pos["row"] - new_pos["row"]):
            return is_valid_path_bishop(gamestate, piece_type, piece_colour, old_pos, new_pos)
        elif piece_type == "q" and ((old_pos["col"] == new_pos["col"] or old_pos["row"] == new_pos["row"]) or
                                    abs(old_pos["col"] - new_pos["col"]) == abs(old_pos["row"] - new_pos["row"])):
            return is_valid_path_queen(gamestate, piece_type, piece_colour, old_pos, new_pos)
        elif piece_type == "k" and (abs(old_pos["col"] - new_pos["col"]) <= 1) and (abs(old_pos["row"] - new_pos["row"]) <= 1) \
                                and gamestate.board[new_pos["col"]][new_pos["row"]][1] != piece_colour:
            return True
        elif (piece_type == "n" and (
                (abs(old_pos["col"] - new_pos["col"]) == 2 and abs(old_pos["row"] - new_pos["row"]) == 1) or
                (abs(old_pos["col"] - new_pos["col"]) == 1 and abs(old_pos["row"] - new_pos["row"]) == 2)) and
              gamestate.board[new_pos["col"]][new_pos["row"]][1] != piece_colour):
            return True

        return False
    return False
