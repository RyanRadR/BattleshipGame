#making a battleship game with basic libraries

import tkinter as tk
import mapBuilder

class BattleshipGame:
    def __init__(self):
        # setup players, boards, etc
        self.window = tk.Tk()
        self.window.title("Battleship")
        self.window.geometry("1000x800-200+100")
        self.window.minsize(300,300)
        self.window.maxsize(1500,1200)


    def run(self):
        #run game loop
        self.create_layout()
        self.window.mainloop()

        #load the screen and display the instructions for setup phase

        mapBuilder.loadPreparationMap()
        print("this is a 2 player game, guess on 10x10 grid where enemy has placed ships")

        #load an empty screen and allow player to guess a location


    def create_layout(self):

        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        self.instr_frame = tk.Frame(self.window, width=200, bg="lightgray")
        self.instr_frame.grid(row=0, column=0, rowspan=2, sticky="ns")
        instr = tk.Label(self.instr_frame, text="Instructions:\nPlace your ships.\nThen guess locations.", justify="left", bg="lightgray")
        instr.pack(padx=10, pady=10)

        self.game_frame = tk.Frame(self.window, bg="white")
        self.game_frame["borderwidth"] = 1
        self.game_frame.grid(row=0, column=1, sticky="nsew")
        self.build_grid()

        self.action_frame = tk.Frame(self.window, height=100, bg="lightblue")
        self.action_frame.grid(row=1, column=1, sticky="ew")
        status = tk.Label(self.action_frame, text="Game status here", bg="lightblue")
        status.pack(pady=10)

    def build_grid(self):
        for row in range(10):
            for col in range(10):
                cell = tk.Button(self.game_frame, text="", width=4, height=2, bg="lightblue")
                cell.grid(row=row, column=col, padx=1, pady=1)

    def show_lobby():
        pass

    def setup_phase():
        pass

    def battle_phase():
        pass

    def end_game():
        pass

