import tkinter as tk
from tkinter import messagebox
import random
global chance


def buttonFunction(number):
    button = btnLst[number - 1]
    if button["cursor"] == "no":
        return
    global chance
    if chance == 9:
        titleLabel["text"] = "Done..."
        button.config(cursor="no", text="X")
        chance += 1
        check()
        return
    if chance % 2 != 0:
        button.config(cursor="no", text="X")
        chance += 1
        titleLabel["text"] = "O's Turn"
        check()
        return
    else:
        button = btnLst[number - 1]
        button.config(cursor="no", text="O")
        chance += 1
        titleLabel["text"] = "X's Turn"
        check()
        return


def playFunction():
    singlePlayerButton.place(x=200, y=200, anchor=tk.CENTER)
    doublePlayerButton.place(x=200, y=230, anchor=tk.CENTER)
    backButton.place(x=200, y=300, anchor=tk.CENTER)


def singlePlayerFunction():
    global chance
    chance = 1
    titleLabel["text"] = "X's Turn"
    backButton["text"] = "Back"
    for btn in btnLst:
        btn.config(text=" ", cursor="hand2")
    button1["command"] = lambda: singlePlayer(1)
    button2["command"] = lambda: singlePlayer(2)
    button3["command"] = lambda: singlePlayer(3)
    button4["command"] = lambda: singlePlayer(4)
    button5["command"] = lambda: singlePlayer(5)
    button6["command"] = lambda: singlePlayer(6)
    button7["command"] = lambda: singlePlayer(7)
    button8["command"] = lambda: singlePlayer(8)
    button9["command"] = lambda: singlePlayer(9)
    button1.place(x=132, y=116, anchor=tk.CENTER)
    button2.place(x=204, y=116, anchor=tk.CENTER)
    button3.place(x=276, y=116, anchor=tk.CENTER)
    button4.place(x=132, y=184, anchor=tk.CENTER)
    button5.place(x=204, y=184, anchor=tk.CENTER)
    button6.place(x=276, y=184, anchor=tk.CENTER)
    button7.place(x=132, y=252, anchor=tk.CENTER)
    button8.place(x=204, y=252, anchor=tk.CENTER)
    button9.place(x=276, y=252, anchor=tk.CENTER)
    return


def doublePlayerFunction():
    global chance
    chance = 1
    titleLabel["text"] = "X's Turn"
    backButton["text"] = "Back"
    for btn in btnLst:
        btn.config(text=" ", cursor="hand2")
    button1["command"] = lambda: buttonFunction(1)
    button2["command"] = lambda: buttonFunction(2)
    button3["command"] = lambda: buttonFunction(3)
    button4["command"] = lambda: buttonFunction(4)
    button5["command"] = lambda: buttonFunction(5)
    button6["command"] = lambda: buttonFunction(6)
    button7["command"] = lambda: buttonFunction(7)
    button8["command"] = lambda: buttonFunction(8)
    button9["command"] = lambda: buttonFunction(9)
    button1.place(x=132, y=116, anchor=tk.CENTER)
    button2.place(x=204, y=116, anchor=tk.CENTER)
    button3.place(x=276, y=116, anchor=tk.CENTER)
    button4.place(x=132, y=184, anchor=tk.CENTER)
    button5.place(x=204, y=184, anchor=tk.CENTER)
    button6.place(x=276, y=184, anchor=tk.CENTER)
    button7.place(x=132, y=252, anchor=tk.CENTER)
    button8.place(x=204, y=252, anchor=tk.CENTER)
    button9.place(x=276, y=252, anchor=tk.CENTER)
    return


def backButtonFunction(button):
    global chance
    if button["text"] == "back":
        chance = 1
        titleLabel["text"] = "Tic Tac Toe"
        singlePlayerButton.place_forget()
        doublePlayerButton.place_forget()
        backButton.place_forget()
        playButton.place(x=200, y=200, anchor=tk.CENTER)
    else:
        chance = 1
        for btn in btnLst:
            btn.place_forget()
        titleLabel["text"] = "Tic Tac Toe"
        singlePlayerButton.place(x=200, y=200, anchor=tk.CENTER)
        doublePlayerButton.place(x=200, y=230, anchor=tk.CENTER)
        backButton["text"] = "back"
        backButton.place(x=200, y=300, anchor=tk.CENTER)
        return


def check():
    global chance
    if button1["text"] == button2["text"] and button2["text"] == button3["text"] and button1["text"] != " ":
        if button1["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button1["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button4["text"] == button5["text"] and button5["text"] == button6["text"] and button4["text"] != " ":
        if button4["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button4["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button7["text"] == button8["text"] and button8["text"] == button9["text"] and button7["text"] != " ":
        if button7["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button7["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button1["text"] == button4["text"] and button4["text"] == button7["text"] and button1["text"] != " ":
        if button1["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button1["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button2["text"] == button5["text"] and button5["text"] == button8["text"] and button2["text"] != " ":
        if button2["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button2["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button3["text"] == button6["text"] and button6["text"] == button9["text"] and button3["text"] != " ":
        if button3["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button3["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button1["text"] == button5["text"] and button5["text"] == button9["text"] and button1["text"] != " ":
        if button1["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button1["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    elif button3["text"] == button5["text"] and button5["text"] == button7["text"] and button3["text"] != " ":
        if button3["text"] == "X":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer1 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
        elif button3["text"] == "O":
            for btn in btnLst:
                btn.config(cursor="no")
            messagebox.showinfo("Winner", "Hurray!\nPlayer2 Has Won the game..\nCongratulations..")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
    else:
        if chance == 10:
            messagebox.showinfo("Winner", "No result.\nGreat! You both done well..\nPlease restart the game.")
            rePlayButton.place(x=200, y=300, anchor=tk.CENTER)
            return


def singlePlayer(number):
    button = btnLst[number - 1]
    if button["cursor"] == "no":
        return
    global chance
    if chance % 2 != 0:
        button.config(text="X", cursor="no")
        chance += 1
        computerPlayer()
        check()


def computerPlayer():
    global chance
    titleLabel["text"] = "X's Turn"
    lst = [btn for btn in btnLst if btn["text"] != 'X' and btn["text"] == " "]
    if len(lst) == 0:
        return
    if btnLst[0]["text"] == "X" and btnLst[1]["text"] == "X" and btnLst[2]["text"] == " ":
        button = btnLst[2]
    elif btnLst[0]["text"] == "X" and btnLst[2]["text"] == "X" and btnLst[1]["text"] == " ":
        button = btnLst[1]
    elif btnLst[1]["text"] == "X" and btnLst[2]["text"] == "X" and btnLst[0]["text"] == " ":
        button = btnLst[0]
    elif btnLst[3]["text"] == "X" and btnLst[4]["text"] == "X" and btnLst[5]["text"] == " ":
        button = btnLst[5]
    elif btnLst[3]["text"] == "X" and btnLst[5]["text"] == "X" and btnLst[4]["text"] == " ":
        button = btnLst[4]
    elif btnLst[4]["text"] == "X" and btnLst[5]["text"] == "X" and btnLst[3]["text"] == " ":
        button = btnLst[3]
    elif btnLst[6]["text"] == "X" and btnLst[7]["text"] == "X" and btnLst[8]["text"] == " ":
        button = btnLst[8]
    elif btnLst[6]["text"] == "X" and btnLst[8]["text"] == "X" and btnLst[7]["text"] == " ":
        button = btnLst[7]
    elif btnLst[7]["text"] == "X" and btnLst[8]["text"] == "X" and btnLst[6]["text"] == " ":
        button = btnLst[6]
    elif btnLst[0]["text"] == "X" and btnLst[3]["text"] == "X" and btnLst[6]["text"] == " ":
        button = btnLst[6]
    elif btnLst[0]["text"] == "X" and btnLst[6]["text"] == "X" and btnLst[3]["text"] == " ":
        button = btnLst[3]
    elif btnLst[3]["text"] == "X" and btnLst[6]["text"] == "X" and btnLst[0]["text"] == " ":
        button = btnLst[0]
    elif btnLst[1]["text"] == "X" and btnLst[4]["text"] == "X" and btnLst[7]["text"] == " ":
        button = btnLst[7]
    elif btnLst[1]["text"] == "X" and btnLst[7]["text"] == "X" and btnLst[4]["text"] == " ":
        button = btnLst[4]
    elif btnLst[4]["text"] == "X" and btnLst[7]["text"] == "X" and btnLst[1]["text"] == " ":
        button = btnLst[1]
    elif btnLst[2]["text"] == "X" and btnLst[5]["text"] == "X" and btnLst[8]["text"] == " ":
        button = btnLst[8]
    elif btnLst[2]["text"] == "X" and btnLst[8]["text"] == "X" and btnLst[5]["text"] == " ":
        button = btnLst[5]
    elif btnLst[5]["text"] == "X" and btnLst[8]["text"] == "X" and btnLst[2]["text"] == " ":
        button = btnLst[2]
    elif btnLst[0]["text"] == "X" and btnLst[4]["text"] == "X" and btnLst[8]["text"] == " ":
        button = btnLst[8]
    elif btnLst[0]["text"] == "X" and btnLst[8]["text"] == "X" and btnLst[4]["text"] == " ":
        button = btnLst[4]
    elif btnLst[4]["text"] == "X" and btnLst[8]["text"] == "X" and btnLst[0]["text"] == " ":
        button = btnLst[0]
    elif btnLst[2]["text"] == "X" and btnLst[4]["text"] == "X" and btnLst[6]["text"] == " ":
        button = btnLst[6]
    elif btnLst[2]["text"] == "X" and btnLst[6]["text"] == "X" and btnLst[4]["text"] == " ":
        button = btnLst[4]
    elif btnLst[4]["text"] == "X" and btnLst[6]["text"] == "X" and btnLst[2]["text"] == " ":
        button = btnLst[2]
    else:
        button = random.choice(lst)
    button.config(text="O", cursor="no")
    chance += 1
    return


def rePlayFunction():
    for btn in btnLst:
        btn.place_forget()
    titleLabel["text"] = "Tic Tac Toe"
    singlePlayerButton.place(x=200, y=200, anchor=tk.CENTER)
    doublePlayerButton.place(x=200, y=230, anchor=tk.CENTER)
    backButton["text"] = "back"
    backButton.place(x=200, y=300, anchor=tk.CENTER)
    rePlayButton.place_forget()
    return


root = tk.Tk()
root.iconbitmap("tic_tac_toe.ico")
root.title("Tic Tac Toe")
root.geometry("400x400")
root.maxsize(400, 400)
root.minsize(400, 400)
titleLabel = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 25, "bold"), fg="black", bg="white")
titleLabel.place(x=208, y=40, anchor=tk.CENTER)
playButton = tk.Button(root, text="Play", fg="green", bg="white", font=("Times new roman", 10, "bold"), cursor="hand2", command=playFunction)
playButton.place(x=200, y=200, anchor=tk.CENTER)
backButton = tk.Button(root, text="back", font=("Times new roman", 10, "bold"), cursor="hand2", command=lambda: backButtonFunction(backButton))
exitButton = tk.Button(root, text="Exit", fg="red", bg="white", font=("Times new roman", 10, "bold"), cursor="hand2", command=root.quit)
exitButton.place(x=200, y=380, anchor=tk.CENTER)
singlePlayerButton = tk.Button(root, text="Single Player", font=("Times new roman", 10, "bold"), cursor="hand2", command=singlePlayerFunction)
doublePlayerButton = tk.Button(root, text="Double Player", font=("Times new roman", 10, "bold"), cursor="hand2", command=doublePlayerFunction)
button1 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(1))
button2 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(2))
button3 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(3))
button4 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(4))
button5 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(5))
button6 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(6))
button7 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(7))
button8 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(8))
button9 = tk.Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(9))
rePlayButton = tk.Button(root, text="Replay", bg="white", fg="black", font=("Times new roman", 10, "bold"), cursor="hand2", command=rePlayFunction)
btnLst = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
chance = 1
root.mainloop()
