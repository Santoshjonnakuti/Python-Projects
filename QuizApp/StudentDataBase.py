import sqlite3


def newUser(userName, fName, lName, mobile, dOB, sQues, sAns, password):
    conn = sqlite3.connect("Students.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Students_DataBase
                (Username text, Firstname text, Lastname text, Mobile text, Date_Of_Birth text, SecurityQuestion text, SQAnswer text, Password text)''')
    cur.execute('''INSERT INTO Students_DataBase VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (userName, fName, lName, mobile, dOB, sQues, sAns, password))
    conn.commit()
    conn.close()
    return


def getStudent(userName):
    conn = sqlite3.connect("Students.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT Password FROM Students_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def getSecurityAnswer(userName):
    conn = sqlite3.connect("Students.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT SQAnswer FROM Students_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def getSecurityQuestion(userName):
    conn = sqlite3.connect("Students.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT SecurityQuestion FROM Students_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def setPassword(userName, password):
    conn = sqlite3.connect("Students.sqlite")
    cur = conn.cursor()
    cur.execute('''UPDATE Students_DataBase SET Password=? WHERE Username=?''', (password, userName))
    conn.commit()
    conn.close()
    return
