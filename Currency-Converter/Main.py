import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup


def Function(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    tags = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    tag = tags.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"})
    data = tag.text
    data = data.split()
    entry1.delete(0, tk.END)
    entry1.insert(0, data[0])
    return


def urlGenerator():
    fro = comboBox.get()
    to = comboBox1.get()
    value = entry.get()
    if fro == "":
        errorLabel["text"] = "From Currency Cannot be empty..."
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    elif to == "":
        errorLabel["text"] = "To Currency Cannot be empty..."
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    elif value == "":
        errorLabel["text"] = "Enter the amount to be converted..."
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    if fro == to:
        errorLabel.place_forget()
        entry1.delete(0, tk.END)
        entry1.insert(0, value)
        return
    fro = fro.split()
    to = to.split()
    url = "https://www.google.com/search?q={}+{}+{}+to+{}+{}".format(value, fro[0], fro[1], to[0], to[1])
    errorLabel.place_forget()
    Function(url)
    return


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
comboBox["state"] = "readonly"
comboBox.place(x=100, y=100, anchor=tk.CENTER)
entry = tk.Entry(root, width=15, bg="white", fg="black", font=("Helvetica", 10))
entry.place(x=83, y=125, anchor=tk.CENTER)

toLabel = tk.Label(root, text="To", bg="black", fg="white", font=("Helvetica", 12, "bold")).place(x=243, y=75, anchor=tk.CENTER)
comboBox1 = ttk.Combobox(root, font=("Helvetica", 8))
comboBox1["values"] = ("Indian Rupee", "US Dollar", "British Pound", "Australian Dollar", "Canadian Dollar", "Japanese Yen", "Swiss Franc")
comboBox1["state"] = "readonly"
comboBox1.place(x=300, y=100, anchor=tk.CENTER)
entry1 = tk.Entry(root, width=15, bg="white", fg="black", font=("Helvetica", 10))
entry1.place(x=283, y=125, anchor=tk.CENTER)

convertButton = tk.Button(root, text="Convert", bg="black", fg="white", font=("Helvetica", 12, "bold"), command=urlGenerator)
convertButton.place(x=450, y=113, anchor=tk.CENTER)
errorLabel = tk.Label(root, text="", bg="black", fg="red", font=("Helvetica", 12))

root.mainloop()
