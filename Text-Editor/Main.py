import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os.path

global path, size


def darkThemeFunction():
    if themeButton["text"] == "Dark Theme":
        themeButton["text"] = "Normal Theme"
        saveButton.config(bg="gray", fg="black")
        saveAsButton.config(bg="gray", fg="black")
        openButton.config(bg="gray", fg="black")
        themeButton.config(bg="gray", fg="black")
        fontSizeIncreaseButton.config(bg="gray", fg="black")
        fontSizeDecreaseButton.config(bg="gray", fg="black")
        boldButton.config(bg="gray", fg="black")
        italicButton.config(bg="gray", fg="black")
        widget.config(bg="black", fg="white", insertbackground="white")
    else:
        themeButton["text"] = "Dark Theme"
        saveButton.config(bg="white", fg="black")
        saveAsButton.config(bg="white", fg="black")
        openButton.config(bg="white", fg="black")
        themeButton.config(bg="white", fg="black")
        fontSizeIncreaseButton.config(bg="white", fg="black")
        fontSizeDecreaseButton.config(bg="white", fg="black")
        boldButton.config(bg="white", fg="black")
        italicButton.config(bg="white", fg="black")
        widget.config(bg="white", fg="black", insertbackground="black")
    return


def saveAsFunction():
    data = widget.get("0.0", tk.END)
    name = entryWidget.get()
    if name == "":
        messagebox.showwarning("Warning!", "Fill out the Entry Box..")
        return
    if ".txt" not in name:
        name = name + ".txt"
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
    global size
    if key == "Increase":
        fontSizeDecreaseButton["cursor"] = "hand2"
        if int(widget["font"][18:20]) != 20:
            widget["font"] = ("Times New Roman", int(widget["font"][18:20]) + 2)
            return
        else:
            fontSizeIncreaseButton["cursor"] = "no"
            return
    elif key == "Decrease":
        fontSizeIncreaseButton["cursor"] = "hand2"
        if int(widget["font"][18:20]) != 10:
            widget["font"] = ("Times New Roman", int(widget["font"][18:20]) - 2)
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


def openButtonFunction():
    global path
    saveButton.config(state=tk.ACTIVE, cursor="hand2")
    filename = filedialog.askopenfilename(initialdir="Desktop", title="Select a File",
                                          filetypes=(("Text files", "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    if filename == '':
        return
    elif ".txt" in filename or ".py" in filename:
        path = filename
        file = open(filename, "r")
        data = file.read()
        widget.delete("0.0", tk.END)
        widget.insert("0.0", data)
        file.close()
        return
    else:
        messagebox.showerror("Error", "Cannot open Such type of Files..")
        return


def saveFunction():
    global path
    if path == '':
        return
    else:
        data = widget.get("0.0", tk.END)
        file = open(path, "w")
        file.write(data)
        file.close()
        return


def styleFunction(key):
    if key == "Bold":
        if widget["font"][21:] == "bold":
            widget.config(font=("Times New Roman", int(widget["font"][18:20])))
            return
        else:
            widget.config(font=("Times New Roman", int(widget["font"][18:20]), "bold"))
            return
    elif key == "Italic":
        if widget["font"][21:] == "italic":
            widget.config(font=("Times New Roman", int(widget["font"][18:20])))
            return
        else:
            widget.config(font=("Times New Roman", int(widget["font"][18:20]), "italic"))
            return


root = tk.Tk()
root.title("Text Editor")
root.iconbitmap("Icon.ico")
frame = tk.Frame(root)
frame.pack()
path = ''
entryWidget = tk.Entry(frame, width=30, bg="white", fg="black")
entryWidget.pack(side=tk.LEFT)
saveButton = tk.Button(frame, text="Save", bg="white", fg="black", command=saveFunction, cursor="no", state=tk.DISABLED)
saveButton.pack(side=tk.LEFT)
saveAsButton = tk.Button(frame, text="Save As", bg="white", fg="black", command=saveAsFunction, cursor="hand2")
saveAsButton.pack(side=tk.LEFT)
openButton = tk.Button(frame, text="Open", bg="white", fg="black", cursor="hand2", command=openButtonFunction)
openButton.pack(side=tk.LEFT)
fontSizeIncreaseButton = tk.Button(frame, text="Increase", bg="white", fg="black",
                                   command=lambda: fontFunction("Increase"), cursor="hand2")
fontSizeIncreaseButton.pack(side=tk.LEFT)
fontSizeDecreaseButton = tk.Button(frame, text="Decrease", bg="white", fg="black",
                                   command=lambda: fontFunction("Decrease"), cursor="hand2")
fontSizeDecreaseButton.pack(side=tk.LEFT)
redImage = ImageTk.PhotoImage(Image.open("red.jpg"))
blueImage = ImageTk.PhotoImage(Image.open("blue.png"))
orangeImage = ImageTk.PhotoImage(Image.open("orange.png"))
cancelImage = ImageTk.PhotoImage(Image.open("Cancel.png"))
redButton = tk.Button(frame, text="red", image=redImage, command=lambda: colorChangeFunction(redButton), cursor="hand2")
redButton.pack(side=tk.LEFT)
blueButton = tk.Button(frame, text="blue", image=blueImage, command=lambda: colorChangeFunction(blueButton),
                       cursor="hand2")
blueButton.pack(side=tk.LEFT)
orangeButton = tk.Button(frame, text="orange", image=orangeImage, command=lambda: colorChangeFunction(orangeButton),
                         cursor="hand2")
orangeButton.pack(side=tk.LEFT)
cancelButton = tk.Button(frame, text="Cancel", image=cancelImage, command=lambda: colorChangeFunction(cancelButton),
                         cursor="hand2")
cancelButton.pack(side=tk.LEFT)
boldButton = tk.Button(frame, text="B", bg="white", fg="black", cursor="hand2", command=lambda: styleFunction("Bold"))
boldButton.pack(side=tk.LEFT)
italicButton = tk.Button(frame, text="I", bg="white", fg="black", command=lambda: styleFunction("Italic"))
italicButton.pack(side=tk.LEFT)
themeButton = tk.Button(frame, text="Dark Theme", bg="white", fg="black", command=darkThemeFunction, cursor="hand2")
themeButton.pack(side=tk.LEFT)
widget = tk.Text(cursor="xterm", font=("Times New Roman", 10))
widget.pack(fill=tk.BOTH, expand=True)
root.mainloop()
