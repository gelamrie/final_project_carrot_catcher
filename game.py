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
        self.canvas.create_image(0, 0, image = self.bg_photo, anchor = 'nw')

        self.rabbit = Rabbit(self.canvas) 
        self.carrots = []  
        self.score = 0 
        self.running = True 

        self.score_text = self.canvas.create_text(10, 10, anchor = "nw", font = ("Arial", 16, "bold"), fill="#33691e", text = "Score: 0")

        self.root.bind("<Left>", lambda e: self.rabbit.move(-20))
        self.root.bind("<Right>", lambda e: self.rabbit.move(20))

        self.quit_button = tk.Button(self.frame, text = "Quit", font =("Arial", 10), command = self.quit_game, bg = "red", fg = "white")
        self.quit_button.place(x = window_width - 60, y = 10)

        self.spawn_carrot()
        self.update()  
        
    def spawn_carrot(self):  
        if not self.running: 
            return   
        x = random.randint(0, window_width - 40)                     
        carrot = Carrot(self.canvas, x, self.drop_speed)
        self.carrots.append(carrot)
        delay = max(300, self.drop_interval + random.randint(-200, 200))  
        self.root.after(delay, self.spawn_carrot)  

    def update(self):
        if not self.running:
            return  
        for carrot in self.carrots[:]:                             
            carrot.fall() 
            if carrot.is_caught_by(self.rabbit):                    
                self.score += 1   
                self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")    
                carrot.delete()                                     
                self.carrots.remove(carrot) 
            elif carrot.is_offscreen():                              
                carrot.delete()                                      
                self.carrots.remove(carrot)      
                self.end_game("Game Over")
        self.root.after(50, self.update)

    def quit_game(self):
        self.running = False
        self.canvas.delete("all")
        self.quit_button.destroy()
        self.canvas.create_text(window_width // 2, window_height // 2 - 20, text = f"Final Score: {self.score}", font = ("Arial", 18, "bold"), fill = "black")  
        self.canvas.create_text(window_width // 2, window_height // 2 + 10, text = "Thanks for playing!", font = ("Arial", 12), fill = "gray")  
        self.try_again_button = tk.Button(self.frame, text = "Try Again", font = ("Arial", 12), command = self.restart_game, bg ="#4CAF50", fg ="white")  
        self.try_again_button.place(x = window_width // 2 - 40, y = window_height // 2 + 40)  
            
    def restart_game(self):
        self.frame.destroy()
        GameMenu(self.root)
    
    def end_game(self, message):  
        self.running = False                                        
        self.quit_button.destroy() 

