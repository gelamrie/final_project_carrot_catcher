import tkinter as tk
from config import window_width, window_height, score_file, difficulty_settings
from game import Game
import os

class GameMenu: 
    def __init__(self, root):                                       
        self.root = root
        self.root.title("Carrot Catcher")            
        self.root.geometry(f"{window_width}x{window_height}")
        self.frame = tk.Frame(root, width = window_width, height = window_height) 
        self.frame.pack()                                  