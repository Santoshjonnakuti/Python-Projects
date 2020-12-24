import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os.path


def darkThemeFunction():
    if themeButton["text"] == "Dark Theme":
        themeButton["text"] = "Normal Theme"
        saveButton.config(bg="gray", fg="black")
        themeButton.config(bg="gray", fg="black")
        fontSizeIncreaseButton.config(bg="gray", fg="black")
        fontSizeDecreaseButton.config(bg="gray", fg="black")
        widget.config(bg="black", fg="white", insertbackground="white")
    else:
        themeButton["text"] = "Dark Theme"
        saveButton.config(bg="white", fg="black")
        themeButton.config(bg="white", fg="black")
        fontSizeIncreaseButton.config(bg="white", fg="black")
        fontSizeDecreaseButton.config(bg="white", fg="black")
        widget.config(bg="white", fg="black", insertbackground="black")
    return


def saveFunction():
    data = widget.get("0.0", tk.END)
    name = entryWidget.get()
    if name == "":
        messagebox.showwarning("Warning!", "Fill out the Entry Box..")
        return
    if ".txt" not in name:
        name = name+".txt"
    else:
        pass
    r = tk.Tk()
    r.withdraw()
    folderSelected = filedialog.askdirectory()
    name = os.path.join(folderSelected, name)
    r.destroy()
    file = open(name, "w")
    file.write(data)
    file.close()


def fontFunction(key):
    if key == "Increase":
        fontSizeDecreaseButton["cursor"] = "hand2"
        if int(widget["font"][18:]) != 20:
            widget["font"] = ("Times New Roman", int(widget["font"][18:])+2)
            return
        else:
            fontSizeIncreaseButton["cursor"] = "no"
            return
    elif key == "Decrease":
        fontSizeIncreaseButton["cursor"] = "hand2"
        if int(widget["font"][18:]) != 10:
            widget["font"] = ("Times New Roman", int(widget["font"][18:])-2)
            return
        else:
            fontSizeDecreaseButton["cursor"] = "no"
            return


def colorChangeFunction(button):
    if button["text"] == "Cancel":
        if themeButton["text"] == "Dark Theme":
            widget.config(fg="black")
            return
        else:
            widget.config(fg="white")
            return
    widget.config(fg=button["text"])
    return


root = tk.Tk()
root.title("Text Editor")
root.iconbitmap("Icon.ico")
frame = tk.Frame(root)
frame.pack()
entryWidget = tk.Entry(frame, width=30, bg="white", fg="black")
entryWidget.pack(side=tk.LEFT)
saveButton = tk.Button(frame, text="Save", bg="white", fg="black", command=saveFunction, cursor="hand2")
saveButton.pack(side=tk.LEFT)
fontSizeIncreaseButton = tk.Button(frame, text="Increase", bg="white", fg="black", command=lambda: fontFunction("Increase"), cursor="hand2")
fontSizeIncreaseButton.pack(side=tk.LEFT)
fontSizeDecreaseButton = tk.Button(frame, text="Decrease", bg="white", fg="black", command=lambda: fontFunction("Decrease"), cursor="hand2")
fontSizeDecreaseButton.pack(side=tk.LEFT)
redImage = ImageTk.PhotoImage(Image.open("red.jpg"))
blueImage = ImageTk.PhotoImage(Image.open("blue.png"))
orangeImage = ImageTk.PhotoImage(Image.open("orange.png"))
cancelImage = ImageTk.PhotoImage(Image.open("Cancel.png"))
redButton = tk.Button(frame, text="red", image=redImage, command=lambda: colorChangeFunction(redButton), cursor="hand2")
redButton.pack(side=tk.LEFT)
blueButton = tk.Button(frame, text="blue", image=blueImage, command=lambda: colorChangeFunction(blueButton), cursor="hand2")
blueButton.pack(side=tk.LEFT)
orangeButton = tk.Button(frame, text="orange", image=orangeImage, command=lambda: colorChangeFunction(orangeButton), cursor="hand2")
orangeButton.pack(side=tk.LEFT)
cancelButton = tk.Button(frame, text="Cancel", image=cancelImage, command=lambda: colorChangeFunction(cancelButton), cursor="hand2")
cancelButton.pack(side=tk.LEFT)
themeButton = tk.Button(frame, text="Dark Theme", bg="white", fg="black", command=darkThemeFunction, cursor="hand2")
themeButton.pack(side=tk.LEFT)
widget = tk.Text(cursor="xterm", font=("Times New Roman", 10))
widget.pack(fill=tk.BOTH, expand=True)
root.mainloop()
