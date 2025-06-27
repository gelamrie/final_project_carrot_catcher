import random 
from PIL import Image, ImageTk
from config import object_size, window_height 

class FallingObject:
    def __init__(self, canvas, x, image_path, speed):
        self.canvas = canvas 
        self.x = x 