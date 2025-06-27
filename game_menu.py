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

        tk.Label(self.frame, text = "Rabbit Catching Carrots", font = ("Arial", 20, "bold")).pack(pady = 20)           

        highscore_label = tk.Label(self.frame, text=  self.get_high_score_text(), font = ("Arial", 12), fg = "gray")  
        highscore_label.pack(pady = 5)                 