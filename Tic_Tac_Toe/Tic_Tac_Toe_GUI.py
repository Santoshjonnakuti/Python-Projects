from tkinter import *
global chance


def check():
    global chance
    if button1["text"] == button2["text"] and button2["text"] == button3["text"] and button1["text"] != " ":
        if button1["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button1["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button4["text"] == button5["text"] and button5["text"] == button6["text"] and button4["text"] != " ":
        if button4["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button4["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button7["text"] == button8["text"] and button8["text"] == button9["text"] and button7["text"] != " ":
        if button7["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button7["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button1["text"] == button4["text"] and button4["text"] == button7["text"] and button1["text"] != " ":
        if button1["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button1["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button2["text"] == button5["text"] and button5["text"] == button8["text"] and button2["text"] != " ":
        if button2["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button2["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button3["text"] == button6["text"] and button6["text"] == button9["text"] and button3["text"] != " ":
        if button3["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button3["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button1["text"] == button5["text"] and button5["text"] == button9["text"] and button1["text"] != " ":
        if button1["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button1["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    elif button3["text"] == button5["text"] and button5["text"] == button7["text"] and button3["text"] != " ":
        if button3["text"] == "X":
            winnerLabel = Label(root, text="Hurray!\nPlayer1 Has Won the game..\nCongratulations..", fg="green")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
        elif button3["text"] == "O":
            winnerLabel = Label(root, text="Hurray!\nPlayer2 Has Won the game..\nCongratulations..", fg="red")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)
            button1["state"] = DISABLED
            button2["state"] = DISABLED
            button3["state"] = DISABLED
            button4["state"] = DISABLED
            button5["state"] = DISABLED
            button6["state"] = DISABLED
            button7["state"] = DISABLED
            button8["state"] = DISABLED
            button9["state"] = DISABLED
    else:
        if chance == 10:
            winnerLabel = Label(root, text="No result.\n Great! You both done well..\nPlease restart the game.", fg="blue")
            winnerLabel.place(relx=0.5, rely=0.8, anchor=CENTER)


def buttonFunction(number):
    global chance
    if number == 1:
        if chance % 2 != 0:
            button1["text"] = "X"
            button1["state"] = DISABLED
            button1["cursor"] = "cross"
            chance += 1
            check()
        else:
            button1["text"] = "O"
            button1["state"] = DISABLED
            button1["cursor"] = "cross"
            chance += 1
            check()
    elif number == 2:
        if chance % 2 != 0:
            button2["text"] = "X"
            button2["state"] = DISABLED
            button2["cursor"] = "cross"
            chance += 1
            check()
        else:
            button2["text"] = "O"
            button2["state"] = DISABLED
            button2["cursor"] = "cross"
            chance += 1
            check()
    elif number == 3:
        if chance % 2 != 0:
            button3["text"] = "X"
            button3["state"] = DISABLED
            button3["cursor"] = "cross"
            chance += 1
            check()
        else:
            button3["text"] = "O"
            button3["state"] = DISABLED
            button3["cursor"] = "cross"
            chance += 1
            check()
    elif number == 4:
        if chance % 2 != 0:
            button4["text"] = "X"
            button4["state"] = DISABLED
            button4["cursor"] = "cross"
            chance += 1
            check()
        else:
            button4["text"] = "O"
            button4["state"] = DISABLED
            button4["cursor"] = "cross"
            chance += 1
            check()
    elif number == 5:
        if chance % 2 != 0:
            button5["text"] = "X"
            button5["state"] = DISABLED
            button5["cursor"] = "cross"
            chance += 1
            check()
        else:
            button5["text"] = "O"
            button5["state"] = DISABLED
            button5["cursor"] = "cross"
            chance += 1
            check()
    elif number == 6:
        if chance % 2 != 0:
            button6["text"] = "X"
            button6["state"] = DISABLED
            button6["cursor"] = "cross"
            chance += 1
            check()
        else:
            button6["text"] = "O"
            button6["state"] = DISABLED
            button6["cursor"] = "cross"
            chance += 1
            check()
    elif number == 7:
        if chance % 2 != 0:
            button7["text"] = "X"
            button7["state"] = DISABLED
            button7["cursor"] = "cross"
            chance += 1
            check()
        else:
            button7["text"] = "O"
            button7["state"] = DISABLED
            button7["cursor"] = "cross"
            chance += 1
            check()
    elif number == 8:
        if chance % 2 != 0:
            button8["text"] = "X"
            button8["state"] = DISABLED
            button8["cursor"] = "cross"
            chance += 1
            check()
        else:
            button8["text"] = "O"
            button8["state"] = DISABLED
            button8["cursor"] = "cross"
            chance += 1
            check()
    else:
        if chance % 2 != 0:
            button9["text"] = "X"
            button9["state"] = DISABLED
            button9["cursor"] = "cross"
            chance += 1
            check()
        else:
            button9["text"] = "O"
            button9["state"] = DISABLED
            button9["cursor"] = "cross"
            chance += 1
            check()


root = Tk()
root.geometry("400x400")
root.title("Tic Tac Toe")
root.iconbitmap("tic_tac_toe.ico")
root.maxsize(400, 400)
root.minsize(400, 400)
titleLabel = Label(root, text="Tic Tac Toe", font=("Helvetica", 25, "bold"), fg="black", bg="white")
titleLabel.place(relx=0.52, rely=0.1, anchor=CENTER)
chance = 1
button1 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(1))
button1.place(relx=0.33, rely=0.29, anchor=CENTER)
button2 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(2))
button2.place(relx=0.51, rely=0.29, anchor=CENTER)
button3 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(3))
button3.place(relx=0.69, rely=0.29, anchor=CENTER)
button4 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(4))
button4.place(relx=0.33, rely=0.46, anchor=CENTER)
button5 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(5))
button5.place(relx=0.51, rely=0.46, anchor=CENTER)
button6 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(6))
button6.place(relx=0.69, rely=0.46, anchor=CENTER)
button7 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(7))
button7.place(relx=0.33, rely=0.63, anchor=CENTER)
button8 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(8))
button8.place(relx=0.51, rely=0.63, anchor=CENTER)
button9 = Button(root, text=" ", padx=30, pady=20, bg="white", cursor="hand2", command=lambda: buttonFunction(9))
button9.place(relx=0.69, rely=0.63, anchor=CENTER)
exitButton = Button(root, text="Exit", fg="black", bg="white", command=root.quit)
exitButton.place(relx=0.5, rely=0.95, anchor=CENTER)
root.mainloop()
