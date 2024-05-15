import tkinter as tk
from tkinter import font

class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cels = {}

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master = display_frame,
            text = "Ready?",
            font = font.Font(size = 28, weight = "bold"),
        )
        self.display.pack()