import tkinter as tk
from Display_Game import DisplayGame

class Menu():
    def __init__(self):
        self.menu = tk.Tk()
        self.menu.title("Menu for Chess Game")

        self.menu.play_button = tk.Button(self.menu, text="Play Chess", font=("Arial", 18), command=self.display_game)
        self.menu.play_button.pack(padx=10, pady=10)

        self.menu.quit_button = tk.Button(self.menu, text="Quit", font=("Arial", 18), command=quit)
        self.menu.quit_button.pack(padx=10, pady=10)




    def display_game(self):
        self.menu.destroy()
        DisplayGame_instance = DisplayGame()
        DisplayGame_instance.run()

    def run(self):
        self.menu.mainloop()
