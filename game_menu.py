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

        tk.Label(self.frame, text="Enter Your Name:", font = ("Arial", 12)).pack(pady = 5) 
        self.name_entry = tk.Entry(self.frame, font = ("Arial", 12))                      
        self.name_entry.pack(pady = 5)     

        tk.Label(self.frame, text = "Choose Difficulty", font = ("Arial", 14, "bold")).pack(pady = 10)  

        for difficulty in difficulty_settings:                                         
            btn = tk.Button(self.frame, text = difficulty, font = ("Arial", 14), width = 15, command = lambda d = difficulty: self.start_game(d))
            btn.pack(pady=5)     

    def get_high_score_text(self):                                    
        if os.path.exists(score_file):
            try:
                with open(score_file, "r") as f:
                    name, score = f.readline().split(":")              
                    return f"Highest Score: {score.strip()} by {name}" 