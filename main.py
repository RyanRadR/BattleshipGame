#making a battleship game with basic libraries

import tkinter as tk
import mapBuilder

windowScreen = tk.Tk()
windowScreen.title("Battleship")
windowScreen.geometry("1000x800-200+100")
windowScreen.minsize(300,300)
windowScreen.maxsize(1500,1200)

windowScreen.mainloop()

frameBoard = tk.Frame()
frameBoard["borderwidth"] = 1

labelInstructions = tk.Label(text="Enter X and Y Guess")


#load the screen and display the instructions for setup phase

mapBuilder.loadPreparationMap()
print("this is a 2 player game, guess on 10x10 grid where enemy has placed ships")


#load an empty screen and allow player to guess a location



