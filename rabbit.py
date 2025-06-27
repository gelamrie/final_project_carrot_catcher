from PIL import Image, Imagetk
from config import rabbit_image_path, window_width, window_height, player_width, player_height

class Rabbit:
    def __init__(self, canvas): 
        self.canvas = canvas
        self.x = window_width // 2  