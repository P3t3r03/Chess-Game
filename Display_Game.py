import tkinter as tk
from tkinter import messagebox
from Load_Images import Images
from Game_State import GameState
from Drag_and_Drop import DnD



class DisplayGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Game")
        self.chess_board_size = 60

        self.canvas = tk.Canvas(self.root, width=8*self.chess_board_size, height=8*self.chess_board_size)
        self.canvas.pack(padx=10, pady=10)
        self.draw_board()
        self.Images = Images()
        self.GameState = GameState()
        self.draw_pieces()
        self.move_pieces = DnD(self.canvas, self.chess_board_size, self.GameState, self.draw_pieces)
        self.root.mainloop()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                x, y = i*self.chess_board_size, j*self.chess_board_size
                colour = "white" if (i + j) % 2 == 0 else "purple"
                self.canvas.create_rectangle(x, y, (x+self.chess_board_size), (y+self.chess_board_size), fill=colour)

    def draw_pieces(self):
        for i in range(8):
            for j in range(8):
                x, y = (i+0.5)*self.chess_board_size, (j+0.5)*self.chess_board_size
                image = self.Images.get_image(self.GameState.board[i][j])
                if image:
                    self.canvas.create_image(x, y, image= image, tags=("token", self.GameState.board[i][j]))

