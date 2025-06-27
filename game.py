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