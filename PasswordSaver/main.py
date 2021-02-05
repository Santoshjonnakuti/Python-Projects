from tkinter import *
import sqlite3
global rootDup
global deleteIdEntry
global msg


def updateFunction():
    applicationName = applicationEntry.get()
    username = userNameEntry.get()
    password = passwordEntry.get()
    conn = sqlite3.connect("PasswordsList.sqlite")
    cur = conn.cursor()
    if applicationName != "" and username != "" and password != "":
        cur.execute('''UPDATE Passwords set Username=?, Password=? WHERE ApplicationOrWebsiteName=?''',
                    (username, password, applicationName))
        messageLabel["text"] = "Successfully Updated..."
        applicationEntry.delete(0, END)
        userNameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        messageLabel.place(relx=0.5, rely=0.72, anchor=CENTER)
    else:
        messageLabel["text"] = "Credinals Cannot be Empty..."
        messageLabel.place(relx=0.5, rely=0.72, anchor=CENTER)
    conn.commit()
    conn.close()


def showAllFunction():
    global rootDup
    global msg
    conn = sqlite3.connect("PasswordsList.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
                        (ApplicationOrWebsiteName text, Username text, Password text)''')
    cur.execute('''SELECT * FROM Passwords;''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    string = ""
    for row in rows:
        application = str(row[0])
        username = str(row[1])
        password = str(row[2])
        string = string + "Application/Website : " + application + "\nUsername : " + username + "\nPassword : " + password +"\n\n"
    print(string)
    rootDup = Tk()
    rootDup.title("Saved Passwords")
    rootDup.iconbitmap("PasswordSavericon.ico")
    msg = Label(rootDup, text=string, anchor=S, justify=LEFT)
    msg.grid(row=0, column=0)
    rootDup.mainloop()


def addFunction():
    conn = sqlite3.connect("PasswordsList.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
            (ApplicationOrWebsiteName text, Username text, Password text)''')
    applicationName = applicationEntry.get()
    username = userNameEntry.get()
    password = passwordEntry.get()
    cur.execute('''SELECT * FROM Passwords;''')
    if applicationName != "" and username != "" and password != "":
        cur.execute('''INSERT INTO Passwords VALUES(?, ?, ?);''',
                    (applicationName, username, password))
        messageLabel["text"] = "Successfully Added..."
        messageLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
        applicationEntry.delete(0, END)
        userNameEntry.delete(0, END)
        passwordEntry.delete(0, END)
    else:
        messageLabel["text"] = "Credinals Cannot be Empty..."
        messageLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
        pass
    conn.commit()
    conn.close()


def deleteIdFunction():
    conn = sqlite3.connect("PasswordsList.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
                        (ApplicationOrWebsiteName text, Username text, Password text)''')
    val = deleteIdEntry.get()
    cur.execute('''DELETE FROM Passwords WHERE ApplicationOrWebsiteName=?''', (val,))
    cur.execute('''SELECT * FROM Passwords''')
    conn.commit()
    conn.close()
    msgLabel = Label(rootDup, text="Successfully Deleted...", bg="white", fg="red")
    msgLabel.grid(row=3, column=0)
    conn = sqlite3.connect("PasswordsList.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
                        (ApplicationOrWebsiteName text, Username text, Password text)''')
    cur.execute('''SELECT * FROM Passwords;''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    string = ""
    for row in rows:
        application = str(row[0])
        username = str(row[1])
        password = str(row[2])
        string = string + "Application/Website : " + application + "\nUsername : " + username + "\nPassword : " + password + "\n\n"

    print(string)
    msg["text"] = string


def deleteFunction():
    global deleteIdEntry
    global rootDup
    global msg
    conn = sqlite3.connect("PasswordsList.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Passwords
                    (ApplicationOrWebsiteName text, Username text, Password text)''')
    cur.execute('''SELECT * FROM Passwords;''')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    string = ""
    for row in rows:
        application = str(row[0])
        username = str(row[1])
        password = str(row[2])
        string = string + "Application/Website : " + application + "\nUsername : " + username + "\nPassword : " + password + "\n\n"

    print(string)
    print(string)
    rootDup = Tk()
    rootDup.title("Saved Passwords")
    rootDup.iconbitmap("PasswordSavericon.ico")
    msg = Label(rootDup, text=string, anchor=S)
    msg.grid(row=0, column=0)
    deleteIdEntry = Entry(rootDup, width=20, bg="white", fg="black")
    deleteIdButton = Button(rootDup, text="Ok", padx=15, command=deleteIdFunction)
    deleteIdEntry.grid(row=1, column=0)
    deleteIdButton.grid(row=2, column=0)
    rootDup.mainloop()


root = Tk()
root.title("Passwords Saver")
root.iconbitmap("PasswordSavericon.ico")
root.geometry("600x150")
root.maxsize(600, 150)
root.minsize(600, 150)
applicationLabel = Label(root, text="Application/Website Name :", bg="white", fg="black")
applicationLabel.place(relx=0.13, rely=0.08, anchor=CENTER)
applicationEntry = Entry(root, width=60)
applicationEntry.place(relx=0.6, rely=0.08, anchor=CENTER)
userNameLabel = Label(root, text="Username :", bg="white", fg="black")
userNameLabel.place(relx=0.06, rely=0.24, anchor=CENTER)
userNameEntry = Entry(root, width=60)
userNameEntry.place(relx=0.6, rely=0.24, anchor=CENTER)
passwordLabel = Label(root, text="Password :", bg="white", fg="black")
passwordLabel.place(relx=0.06, rely=0.40, anchor=CENTER)
passwordEntry = Entry(root, width=60)
passwordEntry.place(relx=0.6, rely=0.40, anchor=CENTER)
updateButton = Button(root, text="Update", bg="white", fg="black", command=updateFunction)
updateButton.place(relx=0.05, rely=0.90, anchor=CENTER)
showAllButton = Button(root, text="Show all", bg="white", fg="black", command=showAllFunction)
showAllButton.place(relx=0.35, rely=0.90, anchor=CENTER)
addButton = Button(root, text="Add", bg="white", fg="black", padx=15, command=addFunction)
addButton.place(relx=0.65, rely=0.90, anchor=CENTER)
deleteButton = Button(root, text="Delete", bg="white", fg="black", command=deleteFunction)
deleteButton.place(relx=0.95, rely=0.90, anchor=CENTER)
messageLabel = Label(root, text=" ", fg="green", bg="white")
root.mainloop()
