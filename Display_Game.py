import tkinter as tk
from tkinter import messagebox
from Load_Images import Images
from Game_State import GameState
from Drag_and_Drop import DnD
import numpy as np


class DisplayGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Game")
        self.chess_board_size = 60

        self.l_taken_canvas = tk.Canvas(self.root, width=8*self.chess_board_size, height=self.chess_board_size)
        self.l_taken_canvas.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(self.root, width=8*self.chess_board_size, height=8*self.chess_board_size)
        self.canvas.pack(padx=10, pady=10)

        self.d_taken_canvas = tk.Canvas(self.root, width=8*self.chess_board_size, height=self.chess_board_size)
        self.d_taken_canvas.pack(padx=10, pady=10)

        # self.piece_importance = {0: 6, 1: 5, 2: 3, 3: 2, 4: 4, 5: 1}
        self.piece_to_string = {0: "k", 1: "q", 2: "r", 3: "b", 4: "n", 5: "p"}
        self.piece_to_value = {0: 1000, 1: 9, 2: 5, 3: 3, 4: 3, 5: 1}

        self.draw_board()
        self.Images = Images()
        self.GameState = GameState()
        self.draw_pieces()
        self.move_pieces = DnD(self.canvas, self.chess_board_size, self.GameState, self.draw_pieces, self.draw_score)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

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
                    self.canvas.create_image(x, y, image=image, tags=("token", self.GameState.board[i][j]))

    def draw_score(self):
        self.l_taken_canvas.delete("taken")
        self.d_taken_canvas.delete("taken")
        d_num_taken, l_num_taken = np.array_split(self.GameState.pieces_taken, 2)

        d_value_taken = sum(self.piece_to_value[i] * num for i, num in enumerate(d_num_taken))
        l_value_taken = sum(self.piece_to_value[i] * num for i, num in enumerate(l_num_taken))
        if d_value_taken > l_value_taken:
            score_text = "+"+str(int(d_value_taken - l_value_taken))
            self.d_taken_canvas.create_text(7.5*self.chess_board_size, 0.5*self.chess_board_size, text=score_text, font=("Arial", 18), tags=("taken",))
        elif d_value_taken < l_value_taken:
            score_text = "+"+str(int(l_value_taken - d_value_taken))
            self.l_taken_canvas.create_text(7.5*self.chess_board_size, 0.5*self.chess_board_size, text=score_text, font=("Arial", 18), tags=("taken",))

        self.draw_taken_pieces(d_num_taken, self.d_taken_canvas, "d")
        self.draw_taken_pieces(l_num_taken, self.l_taken_canvas, "l")

    def draw_taken_pieces(self, num_taken, canvas, player):
        if np.sum(num_taken) <= 7:
            x, y = 0.5 * self.chess_board_size, 0.5 * self.chess_board_size
            for i, num in enumerate(num_taken):
                image = self.Images.get_image(self.piece_to_string[i] + player)
                for _ in range(int(num)):
                    canvas.create_image(x, y, image=image, tags=("taken",))
                    x += self.chess_board_size
        else:
            x, y = 6.75 * self.chess_board_size, 0.5 * self.chess_board_size
            for i in reversed(range(len(num_taken))):  # Iterate in reverse order
                image = self.Images.get_image(self.piece_to_string[i] + player)
                for _ in range(int(num_taken[i])):
                    canvas.create_image(x, y, image=image, tags=("taken",))
                    x -= 7*self.chess_board_size/int(np.sum(num_taken))

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


