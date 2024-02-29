import tkinter as tk
from tkinter import messagebox

class Example(tk.Frame):
    """Illustrate how to drag items on a Tkinter canvas"""

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a canvas
        self.canvas = tk.Canvas(width=400, height=400, background="bisque")
        self.canvas.pack(fill="both", expand=True)

        # this data is used to keep track of an
        # item being dragged
        self._drag_data = {"x": 0, "y": 0, "item": None}

        # create a couple of movable objects
        self.create_token(100, 100, "white")
        self.create_token(200, 100, "black")

        # add bindings for clicking, dragging and releasing over
        # any object with the "token" tag
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.drag_start)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.drag_stop)
        self.canvas.tag_bind("token", "<B1-Motion>", self.drag)

    def create_token(self, x, y, color):
        """Create a token at the given coordinate in the given color"""
        self.canvas.create_oval(
            x - 25,
            y - 25,
            x + 25,
            y + 25,
            outline=color,
            fill=color,
            tags="token"
        )

    def drag_start(self, event):
        """Begining drag of an object"""
        # record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def drag_stop(self, event):
        """End drag of an object"""
        # reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def drag(self, event):
        """Handle dragging of an object"""
        # compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
'''
class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=2, font=('Arial', 15))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Message Box", font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.windowx = 500
        self.windowy = 500
        self.title = "Chess Game"

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def create_window(self):
        pass

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="message", message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.keysym == "Return" and event.state == 4:
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()


MyGUI()




     label = tk.Label(root, text="Win the Game", font=('Arial', 18))
        label.pack(padx=10, pady=20)

        textbox = tk.Text(root, height=2, font=('Arial', 18))
        textbox.pack()

        myentry = tk.Entry(root)
        myentry.pack()

        button = tk.Button(root, text="Click Me", font=('Arial', 18))
        button.pack(padx=10, pady=10)

        buttonframe = tk.Frame(root)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)

        btn1 = tk.Button(buttonframe, text="1", font=('Arial', 15))
        btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        btn2 = tk.Button(buttonframe, text="2", font=('Arial', 15))
        btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        btn3 = tk.Button(buttonframe, text="3", font=('Arial', 15))
        btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

        btn4 = tk.Button(buttonframe, text="4", font=('Arial', 15))
        btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

        btn5 = tk.Button(buttonframe, text="5", font=('Arial', 15))
        btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

        btn6 = tk.Button(buttonframe, text="6", font=('Arial', 15))
        btn6.grid(row=1, column=2, sticky=tk.W + tk.E)
        buttonframe.pack(fill="x")

        anotherbutton = tk.Button(root, text="Stuff")
        anotherbutton.place(x=10, y=10, height=100, width=200)
        root.mainloop()'''
