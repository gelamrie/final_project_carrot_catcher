import random 
from PIL import Image, ImageTk
from config import object_size, window_height 

class FallingObject:
    def __init__(self, canvas, x, image_path, speed):
        self.canvas = canvas 
        self.x = x 
        self.y = 0 
        self.speed = speed 
        img = Image.open(image_path).convert("RGBA").resize((object_size, object_size))
        self.image = ImageTk.PhotoImage(img)
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor='nw')

    def fall(self):
        self.canvas.move(self.id, 0, self.speed)
        self.y = self.canvas.coords(self.id)[1] 

    def is_offscreen(self):
        return self.y > window_height
    
    def delete(self):
        self.canvas.delete(self.id) 
    
    def is_caught_by(self, player):
        obj_coords = self.canvas.bbox(self.id) 
        player_coords = self.canvas.bbox(player.id) 
        if not obj_coords or not player_coords: 
            return False
        return not (
            obj_coords[2] < player_coords[0] or
            obj_coords[0] > player_coords[2] or
            obj_coords[3] < player_coords[1] or 
            obj_coords[1] > player_coords[3] 
        )