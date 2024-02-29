

class GameState():
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.turn = "White"
        self.reset()

    def reset(self):
        self.turn = "White"
        self.board = [[" " for _ in range(8)] for _ in range(8) ]
        self.board[0] = ["rd", "pd", " ", " ", " ", " ", "pl", "rl"]
        self.board[1] = ["nd", "pd", " ", " ", " ", " ", "pl", "nl"]
        self.board[2] = ["bd", "pd", " ", " ", " ", " ", "pl", "bl"]
        self.board[3] = ["qd", "pd", " ", " ", " ", " ", "pl", "ql"]
        self.board[4] = ["kd", "pd", " ", " ", " ", " ", "pl", "kl"]
        self.board[5] = ["bd", "pd", " ", " ", " ", " ", "pl", "bl"]
        self.board[6] = ["nd", "pd", " ", " ", " ", " ", "pl", "nl"]
        self.board[7] = ["rd", "pd", " ", " ", " ", " ", "pl", "rl"]
