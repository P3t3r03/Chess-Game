import tkinter as tk
from Is_Valid_Move import is_valid_move
from Take_Piece import take_piece
from Is_Check import is_check


class DnD:
    def __init__(self, canvas, size, gamestate, draw_pieces, draw_score):
        self.gamestate = gamestate
        self.canvas = canvas
        self.size = size
        self.draw_pieces = draw_pieces
        self.draw_score = draw_score
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_end)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)
        self._drag_data = {"x": 0, "y": 0, "item": None, "piece": None}
        self._initial_position = {"col": 0, "row": 0}
        self._new_position = {"col": 0, "row": 0}
        self.squares_to_highlight = [[False for _ in range(8)] for _ in range(8)]

    def drag_start(self, event):
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self._drag_data["piece"] = self.canvas.gettags(self._drag_data["item"])[1]
        self._initial_position["col"] = self._drag_data["x"]//self.size
        self._initial_position["row"] = self._drag_data["y"]//self.size
        self.highlight_squares()
        self.draw_pieces()
        self.canvas.delete(self.canvas.find_closest(event.x, event.y)[0])

    def drag_end(self, event):

        self._new_position["col"] = event.x//self.size
        self._new_position["row"] = event.y//self.size

        x = self._new_position["col"] * self.size + self.size // 2
        y = self._new_position["row"] * self.size + self.size // 2
        if is_valid_move(self.gamestate, self._drag_data["piece"], self._new_position, self._initial_position):
            self.canvas.coords(self._drag_data["item"], x, y)
            _taken_piece = self.gamestate.board[self._new_position["col"]][self._new_position["row"]]
            take_piece(_taken_piece, self.gamestate)
            self.gamestate.board[self._new_position["col"]][self._new_position["row"]] = self._drag_data["piece"]
            self.gamestate.board[self._initial_position["col"]][self._initial_position["row"]] = "  "
            self.gamestate.turn = not self.gamestate.turn
            self.draw_score()
            self.canvas.delete("highlighted", "token")
            self.draw_pieces()



        else:
            self.canvas.coords(self._drag_data["item"], self._initial_position["col"] * self.size + self.size // 2,
                            self._initial_position["row"] * self.size + self.size // 2)
            self.canvas.delete("highlighted", "token")
            self.draw_pieces()
            self._drag_data["item"] = None
            self._drag_data["piece"] = None
            self._drag_data["x"] = 0
            self._drag_data["y"] = 0

    def drag(self, event):

        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]

        self.canvas.move(self._drag_data["item"], self.size*(delta_x/self.size), self.size*(delta_y/self.size))
        self.canvas.lift(self._drag_data["item"])
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def highlight_squares(self):
        for i in range(8):
            for j in range(8):
                test_pos = {"row": i, "col": j}
                self.squares_to_highlight[i][j] = is_valid_move(self.gamestate, self._drag_data["piece"], test_pos, self._initial_position)
                if self.squares_to_highlight[i][j]:
                    x, y = test_pos["col"] * self.size, test_pos["row"] * self.size
                    self.canvas.create_rectangle(x, y, (x + self.size), (y + self.size),
                                                 fill="green", tag="highlighted")
