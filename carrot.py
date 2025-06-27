from falling_objects import FallingObject 
from config import carrot_image_path 

class Carrot(FallingObject): 
    def __init__(self, canvas, x, speed):
        super().__init__(canvas, x, carrot_image_path, speed) 