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


def getStaff(userName):
    conn = sqlite3.connect("Staff.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT Password FROM Staff_DataBase WHERE Username=?''', (userName,))
    rows = cur.fetchall()
    if not rows:
        val = None
    else:
        val = rows[0][0]
    return val