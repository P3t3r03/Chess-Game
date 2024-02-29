import tkinter as tk


class Images():
    def __init__(self):
        self.bd = tk.PhotoImage(file="Chess Pieces/Chess_bdt60.png")
        self.bl = tk.PhotoImage(file="Chess Pieces/Chess_blt60.png")
        self.kd = tk.PhotoImage(file="Chess Pieces/Chess_kdt60.png")
        self.kl = tk.PhotoImage(file="Chess Pieces/Chess_klt60.png")
        self.nd = tk.PhotoImage(file="Chess Pieces/Chess_ndt60.png")
        self.nl = tk.PhotoImage(file="Chess Pieces/Chess_nlt60.png")
        self.pd = tk.PhotoImage(file="Chess Pieces/Chess_pdt60.png")
        self.pl = tk.PhotoImage(file="Chess Pieces/Chess_plt60.png")
        self.qd = tk.PhotoImage(file="Chess Pieces/Chess_qdt60.png")
        self.ql = tk.PhotoImage(file="Chess Pieces/Chess_qlt60.png")
        self.rd = tk.PhotoImage(file="Chess Pieces/Chess_rdt60.png")
        self.rl = tk.PhotoImage(file="Chess Pieces/Chess_rlt60.png")

    def get_image(self, string):
        return getattr(self, string, None)

