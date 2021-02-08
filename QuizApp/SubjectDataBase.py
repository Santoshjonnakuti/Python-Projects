import sqlite3


def addQuestion(subject, ques, op1, op2, op3, op4, ans):
    conn = sqlite3.connect("Subjects.sqlite")
    cur = conn.cursor()
    cur.execute('''INSERT INTO {} VALUES(?, ?, ?, ?, ?, ?)'''.format(subject), (ques, op1, op2, op3, op4, ans))
    conn.commit()
    conn.close()
    return


def updateQuestion(subject, ques, op1, op2, op3, op4, ans):
    conn = sqlite3.connect("Subjects.sqlite")
    cur = conn.cursor()
    cur.execute('''UPDATE {} SET Option1=?, Option2=?, Option3=?, Option4=?, Answer=? WHERE Question=?'''
                .format(subject), (op1, op2, op3, op4, ans, ques))
    conn.commit()
    conn.close()
    return


def deleteQuestion(subject, ques):
    conn = sqlite3.connect("Subjects.sqlite")
    cur = conn.cursor()
    cur.execute('''DELETE FROM {} WHERE Question=?'''.format(subject), (ques,))
    conn.commit()
    conn.close()
    return


def showAllQuestion(subject):
    conn = sqlite3.connect("Subjects.sqlite")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM {}'''.format(subject))
    questions = cur.fetchall()
    string = ""
    for question in questions:
        string = string + "Question : " + question[0] + "\nOption1 : " + question[1] + "\nOption2 : " + question[2] + \
                 "\nOption3 : " + question[3] + "\nOption4 : " + question[4] + "\nAnswer : " + question[5] + "\n\n"
    return string
