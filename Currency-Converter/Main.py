import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def convertFunction():
    fro = comboBox.get()
    to = comboBox1.get()
    val = entry.get()
    val = float(val)
    if fro == "Indian Rupee":
        pass
    elif fro == "US Dollar":
        val = val * 73.61
    elif fro == "British Pound":
        val = val * 99.62
    elif fro == "Australian Dollar":
        val = val * 56.11
    elif fro == "Canadian Dollar":
        val = val * 57.55
    elif fro == "Japanese Yen":
        val = val * 0.71
    elif fro == "Swiss Franc":
        val = val * 83.33

    if to == "Indian Rupee":
        entry1.delete(0, tk.END)
        entry1.insert(0, val)
    elif to == "US Dollar":
        entry1.delete(0, tk.END)
        entry1.insert(0,  val * 0.014)
    elif to == "British Pound":
        entry1.delete(0, tk.END)
        entry1.insert(0, val * 0.010)
    elif to == "Australian Dollar":
        entry1.delete(0, tk.END)
        entry1.insert(0, val * 0.018)
    elif to == "Canadian Dollar":
        entry1.delete(0, tk.END)
        entry1.insert(0, val * 0.017)
    elif to == "Japanese Yen":
        entry1.delete(0, tk.END)
        entry1.insert(0, val * 1.40)
    elif to == "Swiss Franc":
        entry1.delete(0, tk.END)
        entry1.insert(0, val * 0.012)


root = tk.Tk()
root.title("Currency Converter")
root.iconbitmap("Icon.ico")
root.geometry("600x500")
root.resizable(0, 0)
bgImage = ImageTk.PhotoImage(Image.open("Background.jpg"))
bgLabel = tk.Label(root, image=bgImage).pack()
fromLabel = tk.Label(root, text="From", bg="black", fg="white", font=("Helvetica", 12, "bold")).place(x=53, y=75, anchor=tk.CENTER)
comboBox = ttk.Combobox(root, font=("Helvetica", 8))
comboBox["values"] = ("Indian Rupee", "US Dollar", "British Pound", "Australian Dollar", "Canadian Dollar", "Japanese Yen", "Swiss Franc")
comboBox.place(x=100, y=100, anchor=tk.CENTER)
entry = tk.Entry(root, width=15, bg="white", fg="black", font=("Helvetica", 10))
entry.place(x=83, y=125, anchor=tk.CENTER)
toLabel = tk.Label(root, text="To", bg="black", fg="white", font=("Helvetica", 12, "bold")).place(x=243, y=75, anchor=tk.CENTER)
comboBox1 = ttk.Combobox(root, font=("Helvetica", 8))
comboBox1["values"] = ("Indian Rupee", "US Dollar", "British Pound", "Australian Dollar", "Canadian Dollar", "Japanese Yen", "Swiss Franc")
comboBox1.place(x=300, y=100, anchor=tk.CENTER)
entry1 = tk.Entry(root, width=15, bg="white", fg="black", font=("Helvetica", 10))
entry1.place(x=283, y=125, anchor=tk.CENTER)
convertButton = tk.Button(root, text="Convert", bg="black", fg="white", font=("Helvetica", 12, "bold"), command=convertFunction)
convertButton.place(x=450, y=113, anchor=tk.CENTER)
root.protocol("WN_DELETE_WINDOW", root.destroy)
root.mainloop()
