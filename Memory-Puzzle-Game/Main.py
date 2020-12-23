import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import threading
global buttonList, imageList, numberList, counter, lst, btnLst, counter2, score


def check():
    global counter2, btnLst, score
    time.sleep(1)
    i1 = btnLst[0]["image"]
    i2 = btnLst[1]["image"]
    if i1 == i2:
        counter2 += 1
        btnLst[0].place_forget()
        btnLst[1].place_forget()
        btnLst.pop(0)
        btnLst.pop(0)
        score += 5
        scoreValueLabel["text"] = score
    else:
        btnLst[0].config(image='')
        btnLst[1].config(image='')
        btnLst.pop(0)
        btnLst.pop(0)
        score -= 2
        scoreValueLabel["text"] = score
    if counter2 == 18:
        messageLabel.place(x=300, y=340, anchor=tk.CENTER)
    return


def buttonFunction(button):
    if startButton["state"] != tk.DISABLED:
        return
    global btnLst
    btnLst.append(button)
    num = int(button["text"])
    t = 0
    for tup in lst:
        if num in tup:
            t = lst.index(tup)
            break
    button.config(image=imageList[t-1])
    if len(btnLst) == 2:
        newThread(check)
    return


def arrangeFunction():
    startButton["state"] = tk.DISABLED
    global counter
    for i in range(18):
        val1 = random.choice(numberList)
        numberList.remove(val1)
        val2 = random.choice(numberList)
        numberList.remove(val2)
        buttonList[val1]["image"] = imageList[counter]
        buttonList[val2]["image"] = imageList[counter]
        lst.append((val1, val2))
        counter += 1
        if counter == 18:
            forgetFunction()
    return


def forgetFunction():
    time.sleep(2)
    for i in range(1, 37):
        buttonList[i].config(image='')


def newThread(key):
    NewThread = threading.Thread(target=key)
    NewThread.start()


root = tk.Tk()
root.title("Memory Puzzle Game")
root.geometry("800x700")
root.minsize(800, 700)
root.maxsize(800, 700)
titleLabel = tk.Label(root, text="Memory Puzzle Game", bg="black", fg="white", font=("Helvetica", 43, "bold"))
titleLabel.place(x=300, y=50, anchor=tk.CENTER)
messageLabel = tk.Label(root, text="Game over", bg="white", fg="orange", font=("Helvetica", 35, "bold"))
scoreLabel = tk.Label(root, text="Score", bg="black", fg="white", font=("Helvetica", 15, "bold"))
scoreValueLabel = tk.Label(root, text=0, bg="white", fg="black", font=("Helvetica", 15, "bold"))
img1 = ImageTk.PhotoImage(Image.open("angular.png"))
img2 = ImageTk.PhotoImage(Image.open("c.png"))
img3 = ImageTk.PhotoImage(Image.open("computer.jpg"))
img4 = ImageTk.PhotoImage(Image.open("cpu.png"))
img5 = ImageTk.PhotoImage(Image.open("github.png"))
img6 = ImageTk.PhotoImage(Image.open("html.jpg"))
img7 = ImageTk.PhotoImage(Image.open("java.png"))
img8 = ImageTk.PhotoImage(Image.open("joystick.jpg"))
img9 = ImageTk.PhotoImage(Image.open("mobile.jpg"))
img10 = ImageTk.PhotoImage(Image.open("mouse.jpg"))
img11 = ImageTk.PhotoImage(Image.open("opencv.png"))
img12 = ImageTk.PhotoImage(Image.open("panda.jpg"))
img13 = ImageTk.PhotoImage(Image.open("penguin.jpg"))
img14 = ImageTk.PhotoImage(Image.open("printer.jpg"))
img15 = ImageTk.PhotoImage(Image.open("python.png"))
img16 = ImageTk.PhotoImage(Image.open("satellite.png"))
img17 = ImageTk.PhotoImage(Image.open("telephone.jpg"))
img18 = ImageTk.PhotoImage(Image.open("tv.png"))

startButton = tk.Button(root, text="Start", padx=30, bg="white", fg="black", font=("Helvetica", 27, "bold"), command=lambda: newThread(arrangeFunction))
startButton.place(x=700, y=50, anchor=tk.CENTER)
scoreLabel.place(x=640, y=110, anchor=tk.CENTER)
scoreValueLabel.place(x=690, y=110, anchor=tk.CENTER)
button1 = tk.Button(root, text="1", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button1))
button1.place(x=50, y=150, anchor=tk.CENTER)
button2 = tk.Button(root, text="2", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button2))
button2.place(x=150, y=150, anchor=tk.CENTER)
button3 = tk.Button(root, text="3", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button3))
button3.place(x=250, y=150, anchor=tk.CENTER)
button4 = tk.Button(root, text="4", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button4))
button4.place(x=350, y=150, anchor=tk.CENTER)
button5 = tk.Button(root, text="5", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button5))
button5.place(x=450, y=150, anchor=tk.CENTER)
button6 = tk.Button(root, text="6", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button6))
button6.place(x=550, y=150, anchor=tk.CENTER)

button7 = tk.Button(root, text="7", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button7))
button7.place(x=50, y=250, anchor=tk.CENTER)
button8 = tk.Button(root, text="8", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button8))
button8.place(x=150, y=250, anchor=tk.CENTER)
button9 = tk.Button(root, text="9", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button9))
button9.place(x=250, y=250, anchor=tk.CENTER)
button10 = tk.Button(root, text="10", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button10))
button10.place(x=350, y=250, anchor=tk.CENTER)
button11 = tk.Button(root, text="11", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button11))
button11.place(x=450, y=250, anchor=tk.CENTER)
button12 = tk.Button(root, text="12", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button12))
button12.place(x=550, y=250, anchor=tk.CENTER)

button13 = tk.Button(root, text="13", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button13))
button13.place(x=50, y=350, anchor=tk.CENTER)
button14 = tk.Button(root, text="14", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button14))
button14.place(x=150, y=350, anchor=tk.CENTER)
button15 = tk.Button(root, text="15", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button15))
button15.place(x=250, y=350, anchor=tk.CENTER)
button16 = tk.Button(root, text="16", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button16))
button16.place(x=350, y=350, anchor=tk.CENTER)
button17 = tk.Button(root, text="17", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button17))
button17.place(x=450, y=350, anchor=tk.CENTER)
button18 = tk.Button(root, text="18", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button18))
button18.place(x=550, y=350, anchor=tk.CENTER)

button19 = tk.Button(root, text="19", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button19))
button19.place(x=50, y=450, anchor=tk.CENTER)
button20 = tk.Button(root, text="20", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button20))
button20.place(x=150, y=450, anchor=tk.CENTER)
button21 = tk.Button(root, text="21", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button21))
button21.place(x=250, y=450, anchor=tk.CENTER)
button22 = tk.Button(root, text="22", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button22))
button22.place(x=350, y=450, anchor=tk.CENTER)
button23 = tk.Button(root, text="23", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button23))
button23.place(x=450, y=450, anchor=tk.CENTER)
button24 = tk.Button(root, text="24", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button24))
button24.place(x=550, y=450, anchor=tk.CENTER)

button25 = tk.Button(root, text="25", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button25))
button25.place(x=50, y=550, anchor=tk.CENTER)
button26 = tk.Button(root, text="26", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button26))
button26.place(x=150, y=550, anchor=tk.CENTER)
button27 = tk.Button(root, text="27", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button27))
button27.place(x=250, y=550, anchor=tk.CENTER)
button28 = tk.Button(root, text="28", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button28))
button28.place(x=350, y=550, anchor=tk.CENTER)
button29 = tk.Button(root, text="29", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button29))
button29.place(x=450, y=550, anchor=tk.CENTER)
button30 = tk.Button(root, text="30", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button30))
button30.place(x=550, y=550, anchor=tk.CENTER)

button31 = tk.Button(root, text="31", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button31))
button31.place(x=50, y=650, anchor=tk.CENTER)
button32 = tk.Button(root, text="32", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button32))
button32.place(x=150, y=650, anchor=tk.CENTER)
button33 = tk.Button(root, text="33", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button33))
button33.place(x=250, y=650, anchor=tk.CENTER)
button34 = tk.Button(root, text="34", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button34))
button34.place(x=350, y=650, anchor=tk.CENTER)
button35 = tk.Button(root, text="35", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button35))
button35.place(x=450, y=650, anchor=tk.CENTER)
button36 = tk.Button(root, text="36", padx=40, pady=30, bg="white", fg="white", cursor="hand2", command=lambda: buttonFunction(button36))
button36.place(x=550, y=650, anchor=tk.CENTER)

buttonList = ["", button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
              button12, button13, button14, button15, button16, button17, button18, button19, button20, button21,
              button22, button23, button24, button25, button26, button27, button28, button29, button30, button31,
              button32, button33, button34, button35, button36]
imageList = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16,
             img17, img18]
numberList = [i for i in range(1, 37)]
lst = [(0, 0)]
btnLst = []
counter = 0
counter2 = 0
score = 0
root.mainloop()
