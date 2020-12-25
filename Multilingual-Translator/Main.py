import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup


def Function(url):
    try:
        response = requests.get(url)
    except Exception:
        errorLabel.config(text="No Internet Connection...")
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    soup = BeautifulSoup(response.content, "html.parser")
    tag = soup.find("div", attrs={"class": "MUxGbd u31kKd gsrt lyLwlc", "id": "lrtl-translation-text"})
    if tag is None:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Sorry Cannot translate...")
    else:
        entry1.delete(0, tk.END)
        entry1.insert(0, tag.text)
    return


def urlGenerator():
    url = "https://www.google.com/search?q="
    fro = comboBox.get()
    to = comboBox1.get()
    value = entry.get()
    if fro == "":
        errorLabel["text"] = "From language Cannot be empty..."
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    elif to == "":
        errorLabel["text"] = "To language Cannot be empty..."
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    elif value == "":
        errorLabel["text"] = "Enter the text to be translated..."
        errorLabel.place(x=300, y=300, anchor=tk.CENTER)
        return
    if fro == to:
        errorLabel.place_forget()
        entry1.insert(0, value)
        return
    value = value.split()
    for i in range(len(value)):
        if i != len(value)-1:
            url = url + value[i] + "+"
        else:
            url = url + value[i]
    url = url + "+" + fro + "+to+" + to + "+translate"
    errorLabel.place_forget()
    Function(url)
    return


def getLanguages():
    languagesList = []
    with open("Languages.txt") as file:
        for language in file:
            if "\n" in language:
                languagesList.append(language[:-1])
            else:
                languagesList.append(language)
    return tuple(languagesList)


root = tk.Tk()
root.title("Multilingual Translator")
root.iconbitmap("Icon.ico")
root.geometry("600x500")
root.resizable(0, 0)
bgImage = ImageTk.PhotoImage(Image.open("Background.jpg"))
bgLabel = tk.Label(root, image=bgImage).pack()
languages = getLanguages()
fromLabel = tk.Label(root, text="From", bg="black", fg="white", font=("Helvetica", 12, "bold")).place(x=43, y=75, anchor=tk.CENTER)
comboBox = ttk.Combobox(root, font=("Helvetica", 10))
comboBox["values"] = languages
comboBox["state"] = "readonly"
comboBox.place(x=100, y=100, anchor=tk.CENTER)
entry = tk.Entry(root, width=50, bg="white", fg="black", font=("Helvetica", 10))
entry.place(x=195, y=125, anchor=tk.CENTER)
toLabel = tk.Label(root, text="To", bg="black", fg="white", font=("Helvetica", 12, "bold")).place(x=30, y=175, anchor=tk.CENTER)
comboBox1 = ttk.Combobox(root, font=("Helvetica", 10))
comboBox1["values"] = languages
comboBox1["state"] = "readonly"
comboBox1.place(x=100, y=200, anchor=tk.CENTER)
entry1 = tk.Entry(root, width=50, bg="white", fg="black", font=("Helvetica", 10))
entry1.place(x=195, y=225, anchor=tk.CENTER)
convertButton = tk.Button(root, text="Convert", bg="black", fg="white", font=("Helvetica", 12, "bold"), command=urlGenerator)
convertButton.place(x=450, y=175, anchor=tk.CENTER)
errorLabel = tk.Label(root, text="", bg="black", fg="red", font=("Helvetica", 12))
root.mainloop()
