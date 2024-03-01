from Is_Valid_Move import is_valid_move_colour

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
