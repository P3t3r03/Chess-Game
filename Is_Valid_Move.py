from Is_Valid_Path import *

def is_valid_move(gamestate, piece, new_pos, old_pos):
    piece_colour = piece[1]
    piece_type = piece[0]

    def puts_king_in_check(gamestate, piece, piece_colour, old_pos, new_pos):
        # Make a copy of the gamestate to test the move
        test_gamestate = gamestate.copy()
        # Simulate the move
        test_gamestate.board[new_pos["col"]][new_pos["row"]] = piece
        test_gamestate.board[old_pos["col"]][old_pos["row"]] = "  "
        # Check if the move puts the king in check
        return is_check(test_gamestate, piece_colour)

    if gamestate.turn and piece_colour == "l":
        return is_valid_move_colour(gamestate, piece, new_pos, old_pos) and not puts_king_in_check(gamestate,
                                                                                                   piece,
                                                                                                   piece_colour,
                                                                                                   old_pos, new_pos)
    elif not gamestate.turn and piece_colour == "d":
        return is_valid_move_colour(gamestate, piece, new_pos, old_pos) and not puts_king_in_check(gamestate,
                                                                                                   piece,
                                                                                                   piece_colour,
                                                                                                   old_pos, new_pos)
    return False

def is_check(gamestate, colour):
    king_pos = {"col": -1, "row": -1}
    for i, array in enumerate(gamestate.board):
        for j, element in enumerate(array):
            if element == ("k"+colour):
                king_pos["col"], king_pos["row"] = i, j
                break

    for i in range(8):
        for j in range(8):
            start_pos = {"col": i, "row": j}
            piece = gamestate.board[i][j]
            if is_valid_move_colour(gamestate, piece, king_pos, start_pos):
                return True
    return False

def is_valid_move_colour(gamestate, piece, new_pos, old_pos):
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
        elif piece_type == "k" and (abs(old_pos["col"] - new_pos["col"]) <= 1) and (
                abs(old_pos["row"] - new_pos["row"]) <= 1) \
                and gamestate.board[new_pos["col"]][new_pos["row"]][1] != piece_colour:
            return True
        elif (piece_type == "n" and (
                (abs(old_pos["col"] - new_pos["col"]) == 2 and abs(old_pos["row"] - new_pos["row"]) == 1) or
                (abs(old_pos["col"] - new_pos["col"]) == 1 and abs(old_pos["row"] - new_pos["row"]) == 2)) and
              gamestate.board[new_pos["col"]][new_pos["row"]][1] != piece_colour):
            return True

        return False
    return False
