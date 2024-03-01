def take_piece(string, gamestate):
    piece_map = {
        "kd": 0, "qd": 1, "rd": 2, "bd": 3, "nd": 4, "pd": 5,
        "kl": 6, "ql": 7, "rl": 8, "bl": 9, "nl": 10, "pl": 11
    }

    if string in piece_map:
        index = piece_map[string]
        gamestate.pieces_taken[index] += 1

