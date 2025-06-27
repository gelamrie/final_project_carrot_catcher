import tkinter as tk
import os
import random 
from config import window_width, window_height, score_file, difficulty_settings, background_image_path
from rabbit import Rabbit
from carrot import Carrot
from PIL import Image, ImageTk 
from game_menu import GameMenu 

class Game: 
    def __init__(self, root, difficulty, player_name):   
        self.root = root      
        self.difficulty = difficulty    
        self.player_name = player_name 
        self.drop_speed = difficulty_settings[difficulty]["speed"]
        self.drop_interval = difficulty_settings[difficulty]["interval"]
        
        self.frame = tk.Frame(root, width = window_width, height = window_height)
        self.frame.pack()   

        self.canvas = tk.Canvas(self.frame, width = window_width, height = window_height)
        self.canvas.pack()

        bg_img = Image.open(background_image_path).resize((window_width, window_height)).convert("RGBA")
        bg_img.putalpha(150)  
        self.bg_photo = ImageTk.PhotoImage(bg_img) 