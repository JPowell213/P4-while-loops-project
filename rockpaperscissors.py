# rockpaperscissors.py
#By. Johnathan Powell
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
#creat window
root = Tk()
w = Label(root, text="Rock, Paper, Scissors Test")
w.pack()
#Create Variables
winner = 0
compchoice = 0
player = 0
userchoice = 0
rock = 0
paper = 0
scissors = 0

#welcome
messagebox.showinfo("Welcome","Welcome, your about to play my Rock Paper Scissors Program. This program is simple. \n"
                    "Fist you need to choose what your going to play as, Rock Paper or Scissors. Then the computer with \n"
                    "will pick what it will play as depending on what it chooses you either will win or loose.\n"
               "Rock beats scissors, Scissors beats paper, paper beats rock.")
#the loop start
answer = "y"
while answer == "y":

    #ask player what they want to play as
    player = simpledialog.askstring("player's choice","What do you want to play as? Rock, Paper or scissors.")
    if player == "rock":
        userchoice = "rock"
    elif player == "scissors":
        userchoice = "scissors"
    elif player == "paper":
        userchoice = "paper"
    else:
        messagebox.showinfo("Try again","That's not a choice please choose, rock, paper, or scissors")
    #computer choice

    compchoice = random.choice(("rock","paper","scissors"))

    messagebox.showinfo("user", "The computer chose {}".format(compchoice))
    messagebox.showinfo("user", "the user chose {}".format(userchoice))
    #The works                        
    if compchoice == "rock":
        if userchoice == "paper":
            winner = "user"
        elif userchoice == "scissors":
            winner = "computer"
        else:
            winner = None

    if compchoice == "paper":
        if userchoice == "rock":
            winner = "computer"
        elif userchoice == "scissors":
              winner = "user"
        else:
            winner = None

    if compchoice == "scissors":
        if userchoice == "rock":
            winner = "user"
        elif userchoice == "paper":
            winner = "computer"
        else:
            winner = None
    messagebox.showinfo("winner", "The winner is {}".format(winner))
    answer = simpledialog.askstring("player's choice","Do you want to play again Y/N?")

    answer = answer.strip()
    answer = answer.lower()
    answer = answer[0] 




root.destroy()









    
