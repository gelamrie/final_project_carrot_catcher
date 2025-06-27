from PIL import Image, Imagetk
from config import rabbit_image_path, window_width, window_height, player_width, player_height

class Rabbit:
    def __init__(self, canvas): 
        self.canvas = canvas
        self.x = window_width // 2  
        self.y = window_height - player_height - 10
        img = Image.open(rabbit_image_path).convert("RGBA").resize((player_width, player_height))
        self.image = ImageTk.PhotoImage(img) 
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor='nw')  
    
    def move(self, dx): 