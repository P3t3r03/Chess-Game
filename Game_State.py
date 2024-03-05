import numpy as np

class GameState():
    def __init__(self):
        self.board = [["  " for _ in range(8)] for _ in range(8)]
        self.turn = True  # True for white
        self.pieces_taken = np.zeros(12)  # 0=kd, 1=qd, 2=rd, 3=bd, 4=nd, 5=pd, 6=kl, 7=ql, 8=rl, 9=bl, 10=nl, 11=pl
        self.castling = [False for _ in range(4)]  # 0=tl(Top_Left), 1 = tr, 2=bl, 3=br
        self.reset()

    def reset(self):
        self.turn = "White"
        self.board = [["  " for _ in range(8)] for _ in range(8)]
        self.board[0] = ["rd", "pd", "  ", "  ", "  ", "  ", "pl", "rl"]
        self.board[1] = ["nd", "pd", "  ", "  ", "  ", "  ", "pl", "nl"]
        self.board[2] = ["bd", "pd", "  ", "  ", "  ", "  ", "pl", "bl"]
        self.board[3] = ["qd", "pd", "  ", "  ", "  ", "  ", "pl", "ql"]
        self.board[4] = ["kd", "pd", "  ", "  ", "  ", "  ", "pl", "kl"]
        self.board[5] = ["bd", "pd", "  ", "  ", "  ", "  ", "pl", "bl"]
        self.board[6] = ["nd", "pd", "  ", "  ", "  ", "  ", "pl", "nl"]
        self.board[7] = ["rd", "pd", "  ", "  ", "  ", "  ", "pl", "rl"]
        self.pieces_taken = np.zeros(12)

    def copy(self):

        copied_state = GameState()

        copied_state.board = [col[:] for col in self.board]
        copied_state.castling = [self.castling[i] for i in range(4)]
        print("here") #called 3 times
        print(copied_state.castling)

        return copied_state




