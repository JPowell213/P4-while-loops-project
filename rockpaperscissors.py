# rockpaperscissors.py
#By. Johnathan Powell
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

#Create Variables
winner = 0
computerChoice = 0
player = 0
rock = 0
paper = 0
scissors = 0

#welcome
messagebox.showinfo("Welcome","Welcome, your about to play my Rock Paper Scissors Program. This program is simple. \n"
                    "Fist you need to choose what your going to play as, Rock Paper or Scissors. Then the computer with \n"
                    "will pick what it will play as depending on what it chooses you either will win or loose.\n"
               "Rock beats scissors, Scissors beats paper, paper beats rock.")

 #ask player what they want to play as
player = simpledialog.askstring("player's choice","What do you want to play as? Rock, Paper or scissors.")
if player == "rock":
    player += 1
elif player == "scissors":
    player += 1
elif player == "paper":
    player += 1
else:
    messagebox.showinfo("Try again","That's not a choice please choose, rock, paper, or scissors"
#computer choice

random.randint(1,3)
                        
if computerChoice == 1:
    rock += 1
elif computerChoice == 2:
    scissors += 1
elif computerChoice == 3:
    paper += 1

















    
