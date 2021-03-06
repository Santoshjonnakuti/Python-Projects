import sqlite3


def newStaff(userName, fName, lName, subject, mobile, dOB, sQues, sAns, password):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Staff_DataBase
                (Username text, Firstname text, Lastname text,  Subject text, Mobile text, Date_Of_Birth text, SecurityQuestion text, SQAnswer text, Password text)''')
    cur.execute('''INSERT INTO Staff_DataBase VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (userName, fName, lName, subject, mobile, dOB, sQues, sAns, password))
    conn.commit()
    conn.close()
    return


def getStaffPassword(userName):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT Password FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def getSecurityAnswer(userName):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT SQAnswer FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def getSecurityQuestion(userName):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT SecurityQuestion FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def setPassword(userName, password):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''UPDATE Staff_DataBase SET Password=? WHERE Username=?''', (password, userName))
    conn.commit()
    conn.close()
    return


def createTable(subject):
    conn = sqlite3.connect("Subjects.sqlite")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS {}
                (Question text, Option1 text, Option2 text, Option3 text, Option4 text, Answer text)'''.format(subject))
    conn.commit()
    conn.close()
    return


def getSubject(userName):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT Subject FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    conn.commit()
    conn.close()
    return val


def getName(userName):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT Firstname FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    cur.execute('''SELECT Lastname FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = val + " " + None
    else:
        val = val + " " + rows[0][0]
    conn.commit()
    conn.close()
    return val

