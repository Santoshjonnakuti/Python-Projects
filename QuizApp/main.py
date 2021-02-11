import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import StudentDataBase
import StaffDataBase
import SubjectDataBase

global name, staffName
global questionIndex, questionsList
global presentQuestion
global answerList
previousQuestion = None


def studentShowPasswordFunction(event=None):
    if studentShowPasswordButton["text"] == "Show Password":
        studentShowPasswordButton.config(text="Hide Password")
        studentPasswordEntry.config(show="")
    else:
        studentShowPasswordButton.config(text="Show Password")
        studentPasswordEntry.config(show="*")
    return


def studentSignUpFunction(event=None):
    studentLoginFrame.place_forget()
    staffLoginFrame.place_forget()
    studentSignUpFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def studentLoginFunction(event=None):
    global name
    username = studentUsernameEntry.get()
    password = studentPasswordEntry.get()
    if username == "" or username is None:
        messagebox.showwarning("Warning", "Username Cannot be empty...")
    elif password == "" or password is None:
        messagebox.showwarning("Warning", "Password Cannot be empty...")
    else:
        pwd = StudentDataBase.getStudentPassword(username)
        if pwd == password:
            name = username
            user = StudentDataBase.getName(name)
            studentILInfoLabel["text"] = "Welcome {}".format(user)
            studentILSubjectCombobox["values"] = SubjectDataBase.getAllSubjects()
            studentLoginFrame.place_forget()
            staffLoginFrame.place_forget()
            studentInsideLoginFrame.place(x=750, y=400, anchor=tk.CENTER)
        elif pwd is None:
            messagebox.showerror("Error", "Student not found...")
        elif pwd != password:
            messagebox.showerror("Error", "Incorrect Password")
        pass
    return


def StudentSignUpFunction(event=None):
    fName = firstNameEntry.get()
    lName = lastNameEntry.get()
    emailId = emailIdEntry.get()
    mobile = mobileEntry.get()
    doB = dateOfBirthEntry.get()
    sQues = securityQuestions.get()
    sAns = securityQuesAnsEntry.get()
    pwd = passwordEntry.get()
    rPwd = reEntryPasswordEntry.get()
    if fName == "" or lName == "" or emailId == "" or mobile == "" or sAns == "" or pwd == "" or rPwd == "":
        messagebox.showerror("Error", "All Fields are compulsory...")
        return
    if "@" not in emailId:
        messagebox.showerror("Error", "Invalid Email Id...")
        return
    if len(str(mobile)) != 10:
        messagebox.showerror("Error", "Invalid Mobile Number...")
        return
    if len(str(mobile)) == 10:
        try:
            mobile = int(mobile)
        except ValueError:
            messagebox.showerror("Error", "Invalid Mobile Number...")
            return
    if pwd != rPwd:
        messagebox.showerror("Error", "Password Mismatched...")
        return
    if pwd == rPwd:
        if len(pwd) < 8:
            messagebox.showerror("Error", "Password should have atleast 8 Characters")
            return
        else:
            count = 0
            for c in range(32, 65):
                if chr(c) in pwd:
                    count += 1
                    break
            if count == 0:
                for c in range(91, 97):
                    if chr(c) in pwd:
                        count += 1
                        break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Special Character...")
                return
            count = 0
            for c in range(65, 91):
                if chr(c) in pwd:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Uppercase Character...")
                return
            count = 0
            for c in range(97, 123):
                if chr(c) in pwd:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Lowercase Character...")
                return
    fName = fName[0].upper() + fName[1:]
    lName = lName[0].upper() + lName[1:]
    StudentDataBase.newUser(emailId, fName, lName, mobile, doB, sQues, sAns, pwd)
    messagebox.showinfo("Info", "Successfully Registered...")
    return


def studentSignUpBackFunction(event=None):
    studentSignUpFrame.place_forget()
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


def studentForgotPasswordFunction(event=None):
    global name
    uName = studentUsernameEntry.get()
    if uName == "":
        messagebox.showinfo("Info", "Enter Your Username...")
        return
    else:
        name = uName
        ques = StudentDataBase.getSecurityQuestion(uName)
        if ques is None:
            messagebox.showerror("Error", "User not Found...")
        else:
            studentLoginFrame.place_forget()
            staffLoginFrame.place_forget()
            sFPSQuesLabel["text"] = ques
            studentForgotPasswordFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def studentForgotPasswordBackFunction(event=None):
    studentForgotPasswordFrame.place_forget()
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


def studentForgotPasswordSubmitFunction(event=None):
    ans = sFPSAnsEntry.get()
    if ans == "":
        messagebox.showerror("Error", "Please Input the Answer...")
        return
    sAns = StudentDataBase.getSecurityAnswer(name)
    if ans == sAns:
        studentForgotPasswordFrame.place_forget()
        studentPasswordResetFrame.place(x=700, y=400, anchor=tk.CENTER)
    else:
        messagebox.showerror("Error", "Wrong Answer...")
    return


def studentResetPasswordBackFunction(event=None):
    studentPasswordResetFrame.place_forget()
    studentForgotPasswordFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def studentResetPasswordConfirmFunction(event=None):
    pwd1 = sPRPasswordEntry1.get()
    pwd2 = sPRPasswordEntry2.get()
    if pwd1 == "" or pwd2 == "":
        messagebox.showerror("Error", "All Fields are Compulsory...")
        return
    if pwd1 != pwd2:
        messagebox.showerror("Error", "Password Mismatched...")
        return
    if pwd1 == pwd2:
        if len(pwd1) < 8:
            messagebox.showerror("Error", "Password should have atleast 8 Characters")
            return
        else:
            count = 0
            for c in range(32, 65):
                if chr(c) in pwd1:
                    count += 1
                    break
            if count == 0:
                for c in range(91, 97):
                    if chr(c) in pwd1:
                        count += 1
                        break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Special Character...")
                return
            count = 0
            for c in range(65, 91):
                if chr(c) in pwd1:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Uppercase Character...")
                return
            count = 0
            for c in range(97, 123):
                if chr(c) in pwd1:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Lowercase Character...")
                return
    StudentDataBase.setPassword(name, pwd1)
    messagebox.showinfo("Success!", "Successfully Updated Password...\nGo Back and Login...")
    return


def studentInsideLoginOkFunction(event=None):
    studentILSubjectOkButton["state"] = tk.DISABLED
    global presentQuestion, questionIndex, questionsList, answerList
    studentSubject = studentILSubjectCombobox.get()
    if studentSubject == "" or studentSubject is None:
        messagebox.showerror("Error", "Please Select Subject...")
        return
    else:
        questionsList = SubjectDataBase.getAllQuestion(studentSubject)
        answerList = [None for _ in range(0, len(questionsList) + 1)]
        print(len(answerList))
        print(answerList)
        questionIndex = 0
        presentQuestion = questionsList[questionIndex]
        studentInsideLoginQuestionFrame.place(x=350, y=380, anchor=tk.CENTER)
        studentILPresentQuestionLabel["text"] = str(presentQuestion[0]) + ". " + presentQuestion[1]
        studentILRadioButton1["text"] = presentQuestion[2]
        studentILRadioButton2["text"] = presentQuestion[3]
        studentILRadioButton3["text"] = presentQuestion[4]
        studentILRadioButton4["text"] = presentQuestion[5]
        studentILPresentQuestionLabel.place(x=0, y=20)
        studentILSubmitButton.place(x=1100, y=600)
        return


def studentInsideSubmitFunction(event=None):
    global answerList
    yesNo = messagebox.askyesno("Submit", "Do you want to submit\nOnce submitted answers cannot be changed...")
    if yesNo is True:
        print(answerList)
    else:
        return
    return


def studentInsideLoginNextFunction(event=None):
    global questionIndex, questionsList, presentQuestion, answerList
    if questionIndex != len(questionsList) - 1:
        questionIndex += 1
    else:
        messagebox.showinfo("Information!", "This is the last question...")
        return
    presentQuestion = questionsList[questionIndex]
    studentILPresentQuestionLabel["text"] = str(presentQuestion[0]) + ". " + presentQuestion[1]
    studentILRadioButton1["text"] = presentQuestion[2]
    studentILRadioButton2["text"] = presentQuestion[3]
    studentILRadioButton3["text"] = presentQuestion[4]
    studentILRadioButton4["text"] = presentQuestion[5]
    if answerList[presentQuestion[0]] is None or answerList[presentQuestion[0]] == "0":
        variable.set(None)
    else:
        variable.set(answerList[presentQuestion[0]])
    return


def studentInsideLoginPreviousFunction(event=None):
    global questionIndex, questionsList, presentQuestion, answerList
    if questionIndex != 0:
        questionIndex -= 1
    else:
        messagebox.showinfo("Information!", "This is the First question...")
        return
    presentQuestion = questionsList[questionIndex]
    studentILPresentQuestionLabel["text"] = str(presentQuestion[0]) + ". " + presentQuestion[1]
    studentILRadioButton1["text"] = presentQuestion[2]
    studentILRadioButton2["text"] = presentQuestion[3]
    studentILRadioButton3["text"] = presentQuestion[4]
    studentILRadioButton4["text"] = presentQuestion[5]
    if answerList[presentQuestion[0]] is None or answerList[presentQuestion[0]] == "0":
        variable.set(None)
    else:
        variable.set(answerList[presentQuestion[0]])
    return


def studentInsideLoginClearFunction(event=None):
    global answerList, presentQuestion
    answerList[presentQuestion[0]] = "0"
    variable.set("0")
    print(answerList)
    return


def studentInsideLoginSaveFunction(event=None):
    global presentQuestion, answerList
    print(presentQuestion[0])
    answerList[presentQuestion[0]] = variable.get()
    print(answerList)
    return


def studentInsideLogoutFunction(event=None):
    global answerList
    studentInsideLoginFrame.place_forget()
    studentUsernameEntry.delete(0, tk.END)
    studentPasswordEntry.delete(0, tk.END)
    studentILSubjectOkButton["state"] = tk.ACTIVE
    studentInsideLoginClearFunction()
    studentInsideLoginQuestionFrame.place_forget()
    studentILSubjectCombobox.current(None)
    answerList.clear()
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


def staffShowPasswordFunction(event=None):
    if staffShowPasswordButton["text"] == "Show Password":
        staffShowPasswordButton.config(text="Hide Password")
        staffPasswordEntry.config(show="")
    else:
        staffShowPasswordButton.config(text="Show Password")
        staffPasswordEntry.config(show="*")
    return


def staffSignUpFunction(event=None):
    studentLoginFrame.place_forget()
    staffLoginFrame.place_forget()
    staffSignUpFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def staffLoginFunction(event=None):
    global staffName
    username = staffUsernameEntry.get()
    password = staffPasswordEntry.get()
    if username == "" or username is None:
        messagebox.showwarning("Warning", "Username Cannot be empty...")
    elif password == "" or password is None:
        messagebox.showwarning("Warning", "Password Cannot be empty...")
    else:
        pwd = StaffDataBase.getStaffPassword(username)
        if pwd == password:
            staffName = username
            subject = StaffDataBase.getSubject(staffName)
            user = StaffDataBase.getName(staffName)
            sILInfoLabel["text"] = '''Welcome {},\nYou Can add delete update Questions from your corresponding subject...\nNote : Subject is {}'''.format(user, subject)
            studentLoginFrame.place_forget()
            staffLoginFrame.place_forget()
            sILNoteLabel["text"] = '''Note : Answer should be either 1 or 2 or 3 or 4...\nTo Add/Update a question all fields are compulsory...\nTo Delete a question only question field is compulsory...'''
            staffInsideLoginFrame.place(x=750, y=400, anchor=tk.CENTER)
        elif pwd is None:
            messagebox.showerror("Error", "Staff not found...")
        elif pwd != password:
            messagebox.showerror("Error", "Incorrect Password")
    return


def StaffSignUpFunction(event=None):
    sFName = staffFirstNameEntry.get()
    sLName = staffLastNameEntry.get()
    sEmailId = staffEmailIdEntry.get()
    sMobile = staffMobileEntry.get()
    sDoB = staffDateOfBirthEntry.get()
    sSQues = staffSecurityQuestions.get()
    sSAns = staffSecurityQuesAnsEntry.get()
    sPwd = stafPasswordEntry.get()
    sRPwd = staffReEntryPasswordEntry.get()
    subject = staffSubjectEntry.get()
    if sFName == "" or sLName == "" or sEmailId == "" or sMobile == "" or sSAns == "" or sPwd == "" or sRPwd == "" or subject == "":
        messagebox.showerror("Error", "All Fields are compulsory...")
        return
    if "@" not in sEmailId:
        messagebox.showerror("Error", "Invalid Email Id...")
        return
    if len(str(sMobile)) != 10:
        messagebox.showerror("Error", "Invalid Mobile Number...")
        return
    if len(str(sMobile)) == 10:
        try:
            sMobile = int(sMobile)
        except ValueError:
            messagebox.showerror("Error", "Invalid Mobile Number...")
            return
    count = 0
    for c in range(32, 65):
        if chr(c) in subject:
            count += 1
            break
    if count == 0:
        for c in range(91, 97):
            if chr(c) in subject:
                count += 1
                break
    if " " in subject or count != 0:
        messagebox.showerror("Error",
                             "Special Characters and Spaces are not allowed in Subject...\nSuggestion: User _ or - ...")
        return
    if sPwd != sRPwd:
        messagebox.showerror("Error", "Password Mismatched...")
        return
    if sPwd == sRPwd:
        if len(sPwd) < 8:
            messagebox.showerror("Error", "Password should have atleast 8 Characters")
            return
        else:
            count = 0
            for c in range(32, 65):
                if chr(c) in sPwd:
                    count += 1
                    break
            if count == 0:
                for c in range(91, 97):
                    if chr(c) in sPwd:
                        count += 1
                        break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Special Character...")
                return
            count = 0
            for c in range(65, 91):
                if chr(c) in sPwd:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Uppercase Character...")
                return
            count = 0
            for c in range(97, 123):
                if chr(c) in sPwd:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Lowercase Character...")
                return
    sFName = sFName[0].upper() + sFName[1:]
    sLName = sLName[0].upper() + sLName[1:]
    StaffDataBase.newStaff(sEmailId, sFName, sLName, subject, sMobile, sDoB, sSQues, sSAns, sPwd)
    StaffDataBase.createTable(subject)
    messagebox.showinfo("Info", "Successfully Registered...")
    return


def staffSignUpBackFunction(event=None):
    staffSignUpFrame.place_forget()
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


def staffForgotPasswordFunction(event=None):
    global staffName
    uName = staffUsernameEntry.get()
    if uName == "":
        messagebox.showinfo("Info", "Enter Your Username...")
        return
    else:
        staffName = uName
        ques = StaffDataBase.getSecurityQuestion(uName)
        if ques is None:
            messagebox.showerror("Error", "User not Found...")
        else:
            studentLoginFrame.place_forget()
            staffLoginFrame.place_forget()
            SFPSQuesLabel["text"] = ques
            staffForgotPasswordFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def staffForgotPasswordBackFunction(event=None):
    staffForgotPasswordFrame.place_forget()
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


def staffForgotPasswordSubmitFunction(event=None):
    ans = SFPSAnsEntry.get()
    if ans == "":
        messagebox.showerror("Error", "Please Input the Answer...")
        return
    sAns = StaffDataBase.getSecurityAnswer(staffName)
    if ans == sAns:
        staffForgotPasswordFrame.place_forget()
        staffPasswordResetFrame.place(x=700, y=400, anchor=tk.CENTER)
    else:
        messagebox.showerror("Error", "Wrong Answer...")
    return


def staffResetPasswordBackFunction(event=None):
    staffPasswordResetFrame.place_forget()
    staffForgotPasswordFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def staffResetPasswordConfirmFunction(event=None):
    pwd1 = SPRPasswordEntry1.get()
    pwd2 = SPRPasswordEntry2.get()
    if pwd1 == "" or pwd2 == "":
        messagebox.showerror("Error", "All Fields are Compulsory...")
        return
    if pwd1 != pwd2:
        messagebox.showerror("Error", "Password Mismatched...")
        return
    if pwd1 == pwd2:
        if len(pwd1) < 8:
            messagebox.showerror("Error", "Password should have atleast 8 Characters")
            return
        else:
            count = 0
            for c in range(32, 65):
                if chr(c) in pwd1:
                    count += 1
                    break
            if count == 0:
                for c in range(91, 97):
                    if chr(c) in pwd1:
                        count += 1
                        break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Special Character...")
                return
            count = 0
            for c in range(65, 91):
                if chr(c) in pwd1:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Uppercase Character...")
                return
            count = 0
            for c in range(97, 123):
                if chr(c) in pwd1:
                    count += 1
                    break
            if count == 0:
                messagebox.showerror("Error", "Password should have atleast 1 Lowercase Character...")
                return
    StaffDataBase.setPassword(staffName, pwd1)
    messagebox.showinfo("Success!", "Successfully Updated Password...\nGo Back and Login...")
    return


def staffInsideLoginAddFunction(event=None):
    ques = sILQuestionEntry.get()
    op1 = sILOption1Entry.get()
    op2 = sILOption2Entry.get()
    op3 = sILOption3Entry.get()
    op4 = sILOption4Entry.get()
    ans = sILAnswerEntry.get()
    if ques == "" or op1 == "" or op2 == "" or op3 == "" or op4 == "" or ans == "":
        messagebox.showerror("Error", "All Fields are compulsory...")
        return
    if ans != "1" and ans != "2" and ans != "3" and ans != "4":
        messagebox.showerror("Error", "Answer should be either 1 or 2 or 3 or 4...")
        return
    Subject = StaffDataBase.getSubject(staffName)
    SubjectDataBase.addQuestion(Subject, ques, op1, op2, op3, op4, ans)
    messagebox.showinfo("Success!", "Question Added Successfully...")
    sILQuestionEntry.delete(0, tk.END)
    sILOption1Entry.delete(0, tk.END)
    sILOption2Entry.delete(0, tk.END)
    sILOption3Entry.delete(0, tk.END)
    sILOption4Entry.delete(0, tk.END)
    sILAnswerEntry.delete(0, tk.END)
    return


def staffInsideLoginUpdateFunction(event=None):
    ques = sILQuestionEntry.get()
    op1 = sILOption1Entry.get()
    op2 = sILOption2Entry.get()
    op3 = sILOption3Entry.get()
    op4 = sILOption4Entry.get()
    ans = sILAnswerEntry.get()
    if ques == "" or op1 == "" or op2 == "" or op3 == "" or op4 == "" or ans == "":
        messagebox.showerror("Error", "All Fields are compulsory...")
        return
    Subject = StaffDataBase.getSubject(staffName)
    SubjectDataBase.updateQuestion(Subject, ques, op1, op2, op3, op4, ans)
    messagebox.showinfo("Success!", "Question Updated Successfully...")
    sILQuestionEntry.delete(0, tk.END)
    sILOption1Entry.delete(0, tk.END)
    sILOption2Entry.delete(0, tk.END)
    sILOption3Entry.delete(0, tk.END)
    sILOption4Entry.delete(0, tk.END)
    sILAnswerEntry.delete(0, tk.END)
    return


def staffInsideLoginDeleteFunction(event=None):
    ques = sILQuestionEntry.get()
    if ques == "":
        messagebox.showerror("Error", "Please Enter Question...")
        return
    Subject = StaffDataBase.getSubject(staffName)
    SubjectDataBase.deleteQuestion(Subject, ques)
    messagebox.showinfo("Success!", "Question Deleted Successfully...")
    sILQuestionEntry.delete(0, tk.END)
    sILOption1Entry.delete(0, tk.END)
    sILOption2Entry.delete(0, tk.END)
    sILOption3Entry.delete(0, tk.END)
    sILOption4Entry.delete(0, tk.END)
    sILAnswerEntry.delete(0, tk.END)
    return


def staffInsideLoginShowAllFunction(event=None):
    nWindow = tk.Tk()
    nWindow.title("Questions")
    nWindow.iconbitmap("Icon.ico")
    Subject = StaffDataBase.getSubject(staffName)
    string = SubjectDataBase.showAllQuestion(Subject)
    showAllWidget = tk.Text(nWindow, bg="white", fg="black", font=("Times New Roman", 12), cursor="hand2")
    showAllWidget.delete("0.0", tk.END)
    showAllWidget.insert("0.0", string)
    showAllWidget.pack(fill=tk.X, expand=True)
    nWindow.mainloop()
    return


def staffInsideLogoutFunction(event=None):
    staffInsideLoginFrame.place_forget()
    staffUsernameEntry.delete(0, tk.END)
    staffPasswordEntry.delete(0, tk.END)
    sILQuestionEntry.delete(0, tk.END)
    sILOption1Entry.delete(0, tk.END)
    sILOption2Entry.delete(0, tk.END)
    sILOption3Entry.delete(0, tk.END)
    sILOption4Entry.delete(0, tk.END)
    sILAnswerEntry.delete(0, tk.END)
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


root = tk.Tk()
root.geometry("1500x800")
root.title("Quiz")
root.iconbitmap("Icon.ico")
bgImage = ImageTk.PhotoImage(Image.open("Background.jpg"))
bgLabel = tk.Label(root, image=bgImage).pack()

# Student Login Frame
studentLoginFrame = tk.LabelFrame(root, text="Student Login", bg="white", fg="#83aff7", height=600, width=500,
                                  font=("Times New Roman", 20, "bold"))
studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)

studentUsernameLabel = tk.Label(studentLoginFrame, text="Username", bg="white", fg="#43518c",
                                font=("Times New Roman", 15, "bold"))
studentUsernameLabel.place(x=50, y=40, anchor=tk.CENTER)
studentUsernameEntry = tk.Entry(studentLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED)
studentUsernameEntry.place(x=170, y=80, anchor=tk.CENTER)
studentPasswordLabel = tk.Label(studentLoginFrame, text="Password", bg="white", fg="#43518c",
                                font=("Times New Roman", 15, "bold"))
studentPasswordLabel.place(x=50, y=120, anchor=tk.CENTER)
studentPasswordEntry = tk.Entry(studentLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED,
                                show="*")
studentPasswordEntry.place(x=170, y=160, anchor=tk.CENTER)
studentShowPasswordButton = tk.Button(studentLoginFrame, text="Show Password", bg="white", fg="black", bd=0,
                                      font=("Times New Roman", 10), cursor="hand2", command=studentShowPasswordFunction)
studentShowPasswordButton.bind("<Return>", studentShowPasswordFunction)
studentShowPasswordButton.place(x=400, y=160, anchor=tk.CENTER)
studentForgotPasswordButton = tk.Button(studentLoginFrame, text="Forgot Password?", bg="white", fg="#453c85", bd=0,
                                        font=("Times New Roman", 10), cursor="hand2",
                                        command=studentForgotPasswordFunction)
studentForgotPasswordButton.bind("<Return>", studentForgotPasswordFunction)
studentForgotPasswordButton.place(x=285, y=190, anchor=tk.CENTER)
studentLoginButton = tk.Button(studentLoginFrame, text="Log In", bg="white", fg="#4b396e", font=("Times New Roman", 12),
                               cursor="hand2", bd=0, command=studentLoginFunction)
studentLoginButton.bind("<Return>", studentLoginFunction)
studentLoginButton.place(x=30, y=220, anchor=tk.CENTER)
studentSignUpButton = tk.Button(studentLoginFrame, text="Don't have an account? Sign up", bg="white", fg="#4b396e",
                                bd=0, cursor="hand2", font=("Times New Roman", 10), command=studentSignUpFunction)
studentSignUpButton.bind("<Return>", studentSignUpFunction)
studentSignUpButton.place(x=95, y=260, anchor=tk.CENTER)

# Staff Login Frame
staffLoginFrame = tk.LabelFrame(root, text="Staff Login", bg="white", fg="#83aff7", height=600, width=500,
                                font=("Times New Roman", 20, "bold"))
staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)

staffUsernameLabel = tk.Label(staffLoginFrame, text="Username", bg="white", fg="#43518c",
                              font=("Times New Roman", 15, "bold"))
staffUsernameLabel.place(x=50, y=40, anchor=tk.CENTER)
staffUsernameEntry = tk.Entry(staffLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED)
staffUsernameEntry.place(x=170, y=80, anchor=tk.CENTER)
staffPasswordLabel = tk.Label(staffLoginFrame, text="Password", bg="white", fg="#43518c",
                              font=("Times New Roman", 15, "bold"))
staffPasswordLabel.place(x=50, y=120, anchor=tk.CENTER)
staffPasswordEntry = tk.Entry(staffLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED,
                              show="*")
staffPasswordEntry.place(x=170, y=160, anchor=tk.CENTER)
staffShowPasswordButton = tk.Button(staffLoginFrame, text="Show Password", bg="white", fg="black", bd=0,
                                    font=("Times New Roman", 10), cursor="hand2", command=staffShowPasswordFunction)
staffShowPasswordButton.bind("<Return>", staffShowPasswordFunction)
staffShowPasswordButton.place(x=400, y=160, anchor=tk.CENTER)
staffForgotPasswordButton = tk.Button(staffLoginFrame, text="Forgot Password?", bg="white", fg="#453c85", bd=0,
                                      font=("Times New Roman", 10), cursor="hand2", command=staffForgotPasswordFunction)
staffForgotPasswordButton.bind("<Return>", studentForgotPasswordFunction)
staffForgotPasswordButton.place(x=285, y=190, anchor=tk.CENTER)
staffLoginButton = tk.Button(staffLoginFrame, text="Log In", bg="white", fg="#4b396e", font=("Times New Roman", 12),
                             cursor="hand2", bd=0, command=staffLoginFunction)
staffLoginButton.bind("<Return>", staffLoginFunction)
staffLoginButton.place(x=30, y=220, anchor=tk.CENTER)
staffSignUpButton = tk.Button(staffLoginFrame, text="Don't have an account? Sign up", bg="white", fg="#4b396e", bd=0,
                              cursor="hand2", font=("Times New Roman", 10), command=staffSignUpFunction)
staffSignUpButton.bind("<Return>", staffSignUpFunction)
staffSignUpButton.place(x=95, y=260, anchor=tk.CENTER)

# Student Sign up Frame
studentSignUpFrame = tk.LabelFrame(root, text="Sign up", bg="white", fg="#83aff7", height=600, width=500,
                                   font=("Times New Roman", 20, "bold"))
firstNameLabel = tk.Label(studentSignUpFrame, text="Firstname", bg="white", fg="black", font=("Times New Roman", 12))
firstNameLabel.place(x=100, y=80, anchor=tk.CENTER)
firstNameEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
firstNameEntry.place(x=290, y=80, anchor=tk.CENTER)
lastNameLabel = tk.Label(studentSignUpFrame, text="Lastname", bg="white", fg="black", font=("Times New Roman", 12))
lastNameLabel.place(x=100, y=120, anchor=tk.CENTER)
lastNameEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
lastNameEntry.place(x=290, y=120, anchor=tk.CENTER)
emailIdLabel = tk.Label(studentSignUpFrame, text="Email", bg="white", fg="black", font=("Times New Roman", 12))
emailIdLabel.place(x=113, y=160, anchor=tk.CENTER)
emailIdEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
emailIdEntry.place(x=290, y=160, anchor=tk.CENTER)
mobileLabel = tk.Label(studentSignUpFrame, text="Mobile No.", bg="white", fg="black", font=("Times New Roman", 12))
mobileLabel.place(x=96, y=200, anchor=tk.CENTER)
mobileEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
mobileEntry.place(x=290, y=200, anchor=tk.CENTER)
dateOfBirthLabel = tk.Label(studentSignUpFrame, text="Date of Birth", bg="white", fg="black",
                            font=("Times New Roman", 12))
dateOfBirthLabel.place(x=95, y=240, anchor=tk.CENTER)
dateOfBirthEntry = DateEntry(studentSignUpFrame, width=42, bg="black", fg="white", year=2000, state="readonly")
dateOfBirthEntry.place(x=305, y=240, anchor=tk.CENTER)
securityQuestionsLabel = tk.Label(studentSignUpFrame, text="Security Question", bg="white", fg="black",
                                  font=("Times New Roman", 12))
securityQuestionsLabel.place(x=82, y=280, anchor=tk.CENTER)
securityQuestions = ttk.Combobox(studentSignUpFrame, width=30, state="readonly", font=("Times New Roman", 12))
securityQuestions["values"] = tuple(["What is your lastname?", "What is your Pet name?", "What is your nickname?"])
securityQuestions.current(0)
securityQuestions.place(x=300, y=280, anchor=tk.CENTER)
securityQuesAnsLabel = tk.Label(studentSignUpFrame, text="Answer", fg="black", bg="white", font=("Times New Roman", 12))
securityQuesAnsLabel.place(x=113, y=320, anchor=tk.CENTER)
securityQuesAnsEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                                bg="white")
securityQuesAnsEntry.place(x=290, y=320, anchor=tk.CENTER)
passwordLabel = tk.Label(studentSignUpFrame, text="Password", bg="white", fg="black", font=("Times New Roman", 12))
passwordLabel.place(x=108, y=360, anchor=tk.CENTER)
passwordEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
passwordEntry.place(x=290, y=360, anchor=tk.CENTER)
reEntryPasswordLabel = tk.Label(studentSignUpFrame, text="Re-enter Password", bg="white", fg="black",
                                font=("Times New Roman", 12))
reEntryPasswordLabel.place(x=80, y=400, anchor=tk.CENTER)
reEntryPasswordEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                                bg="white")
reEntryPasswordEntry.place(x=290, y=400, anchor=tk.CENTER)
signUpButton = tk.Button(studentSignUpFrame, text="Sign up", bg="white", fg="black", font=("Times New Roman", 12),
                         cursor="hand2", bd=0, command=StudentSignUpFunction)
signUpButton.bind("<Return>", StudentSignUpFunction)
signUpButton.place(x=240, y=440, anchor=tk.CENTER)
signUpBackButton = tk.Button(studentSignUpFrame, text="Back", fg="black", bg="white", font=("Times New Roman", 12),
                             cursor="hand2", bd=0, command=studentSignUpBackFunction)
signUpBackButton.bind("<Return>", studentSignUpBackFunction)
signUpBackButton.place(x=240, y=480, anchor=tk.CENTER)

# Staff Sign up Frame
staffSignUpFrame = tk.LabelFrame(root, text="Sign up", bg="white", fg="#83aff7", height=600, width=500,
                                 font=("Times New Roman", 20, "bold"))
staffFirstNameLabel = tk.Label(staffSignUpFrame, text="Firstname", bg="white", fg="black", font=("Times New Roman", 12))
staffFirstNameLabel.place(x=100, y=80, anchor=tk.CENTER)
staffFirstNameEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffFirstNameEntry.place(x=290, y=80, anchor=tk.CENTER)
staffLastNameLabel = tk.Label(staffSignUpFrame, text="Lastname", bg="white", fg="black", font=("Times New Roman", 12))
staffLastNameLabel.place(x=100, y=120, anchor=tk.CENTER)
staffLastNameEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffLastNameEntry.place(x=290, y=120, anchor=tk.CENTER)
staffEmailIdLabel = tk.Label(staffSignUpFrame, text="Email", bg="white", fg="black", font=("Times New Roman", 12))
staffEmailIdLabel.place(x=113, y=160, anchor=tk.CENTER)
staffEmailIdEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffEmailIdEntry.place(x=290, y=160, anchor=tk.CENTER)
staffMobileLabel = tk.Label(staffSignUpFrame, text="Mobile No.", bg="white", fg="black", font=("Times New Roman", 12))
staffMobileLabel.place(x=96, y=200, anchor=tk.CENTER)
staffMobileEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffMobileEntry.place(x=290, y=200, anchor=tk.CENTER)
staffDateOfBirthLabel = tk.Label(staffSignUpFrame, text="Date of Birth", bg="white", fg="black",
                                 font=("Times New Roman", 12))
staffDateOfBirthLabel.place(x=95, y=240, anchor=tk.CENTER)
staffDateOfBirthEntry = DateEntry(staffSignUpFrame, width=42, bg="black", fg="white", year=2000, state="readonly")
staffDateOfBirthEntry.place(x=305, y=240, anchor=tk.CENTER)
staffSecurityQuestionsLabel = tk.Label(staffSignUpFrame, text="Security Question", bg="white", fg="black",
                                       font=("Times New Roman", 12))
staffSecurityQuestionsLabel.place(x=82, y=280, anchor=tk.CENTER)
staffSecurityQuestions = ttk.Combobox(staffSignUpFrame, width=30, state="readonly", font=("Times New Roman", 12))
staffSecurityQuestions["values"] = tuple(["What is your lastname?", "What is your Pet name?", "What is your nickname?"])
staffSecurityQuestions.current(0)
staffSecurityQuestions.place(x=300, y=280, anchor=tk.CENTER)
staffSecurityQuesAnsLabel = tk.Label(staffSignUpFrame, text="Answer", fg="black", bg="white",
                                     font=("Times New Roman", 12))
staffSecurityQuesAnsLabel.place(x=113, y=320, anchor=tk.CENTER)
staffSecurityQuesAnsEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                                     bg="white")
staffSecurityQuesAnsEntry.place(x=290, y=320, anchor=tk.CENTER)
stafPasswordLabel = tk.Label(staffSignUpFrame, text="Password", bg="white", fg="black", font=("Times New Roman", 12))
stafPasswordLabel.place(x=108, y=360, anchor=tk.CENTER)
stafPasswordEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
stafPasswordEntry.place(x=290, y=360, anchor=tk.CENTER)
staffReEntryPasswordLabel = tk.Label(staffSignUpFrame, text="Re-enter Password", bg="white", fg="black",
                                     font=("Times New Roman", 12))
staffReEntryPasswordLabel.place(x=80, y=400, anchor=tk.CENTER)
staffReEntryPasswordEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                                     bg="white")
staffReEntryPasswordEntry.place(x=290, y=400, anchor=tk.CENTER)
staffSubjectLabel = tk.Label(staffSignUpFrame, text="Subject", bg="white", fg="black", font=("Times New Roman", 12))
staffSubjectLabel.place(x=108, y=440, anchor=tk.CENTER)
staffSubjectEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffSubjectEntry.place(x=290, y=440, anchor=tk.CENTER)
staffSignUpButton = tk.Button(staffSignUpFrame, text="Sign up", bg="white", fg="black", font=("Times New Roman", 12),
                              cursor="hand2", bd=0, command=StaffSignUpFunction)
staffSignUpButton.bind("<Return>", StaffSignUpFunction)
staffSignUpButton.place(x=240, y=480, anchor=tk.CENTER)
staffSignUpBackButton = tk.Button(staffSignUpFrame, text="Back", fg="black", bg="white", font=("Times New Roman", 12),
                                  cursor="hand2", bd=0, command=staffSignUpBackFunction)
staffSignUpBackButton.bind("<Return>", staffSignUpBackFunction)
staffSignUpBackButton.place(x=240, y=520, anchor=tk.CENTER)

# Student Forgot Password Frame
studentForgotPasswordFrame = tk.LabelFrame(root, text="Forgot Password", bg="white", fg="#83aff7", height=600,
                                           width=500, font=("Times New Roman", 20, "bold"))
sFPSQuesLabel = tk.Label(studentForgotPasswordFrame, text="What is Your lastname?", bg="white", fg="black",
                         font=("Times New Roman", 12))
sFPSQuesLabel.place(x=240, y=80, anchor=tk.CENTER)
sFPSAnsEntry = tk.Entry(studentForgotPasswordFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                        bg="white")
sFPSAnsEntry.place(x=240, y=120, anchor=tk.CENTER)
sFPSubmitButton = tk.Button(studentForgotPasswordFrame, text="Submit", fg="black", bg="white", bd=0, cursor="hand2",
                            font=("Times New Roman", 12), command=studentForgotPasswordSubmitFunction)
sFPSubmitButton.bind("<Return>", studentForgotPasswordSubmitFunction)
sFPSubmitButton.place(x=240, y=160, anchor=tk.CENTER)
sFPBackButton = tk.Button(studentForgotPasswordFrame, text="Back", bg="white", fg="black", font=("Times New Roman", 12),
                          bd=0, cursor="hand2", command=studentForgotPasswordBackFunction)
sFPBackButton.bind("<Return>", studentForgotPasswordBackFunction)
sFPBackButton.place(x=240, y=200, anchor=tk.CENTER)

# Student Password Reset Frame
studentPasswordResetFrame = tk.LabelFrame(root, text="Reset Password", bg="white", fg="#83aff7", height=600, width=500,
                                          font=("Times New Roman", 20, "bold"))
sPRPasswordLabel = tk.Label(studentPasswordResetFrame, text="Enter the password below", bg="white", fg="black",
                            font=("Times New Roman", 12))
sPRPasswordLabel.place(x=240, y=80, anchor=tk.CENTER)
sPRPasswordEntry1 = tk.Entry(studentPasswordResetFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                             bg="white")
sPRPasswordEntry1.place(x=240, y=120, anchor=tk.CENTER)
sPRPasswordEntry2 = tk.Entry(studentPasswordResetFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                             bg="white")
sPRPasswordEntry2.place(x=240, y=160, anchor=tk.CENTER)
sPRConfirmButton = tk.Button(studentPasswordResetFrame, text="Confirm", bg="white", fg="black", bd=0, cursor="hand2",
                             font=("Times New Roman", 12), command=studentResetPasswordConfirmFunction)
sPRConfirmButton.bind("<Return>", studentResetPasswordConfirmFunction)
sPRConfirmButton.place(x=240, y=200, anchor=tk.CENTER)
sPRBackButton = tk.Button(studentPasswordResetFrame, text="Back", bg="white", fg="black", bd=0, cursor="hand2",
                          font=("Times New Roman", 12), command=studentResetPasswordBackFunction)
sPRBackButton.bind("<Return>", studentResetPasswordBackFunction)
sPRBackButton.place(x=240, y=240, anchor=tk.CENTER)

# Staff Forgot Password Frame
staffForgotPasswordFrame = tk.LabelFrame(root, text="Forgot Password", bg="white", fg="#83aff7", height=600, width=500,
                                         font=("Times New Roman", 20, "bold"))
SFPSQuesLabel = tk.Label(staffForgotPasswordFrame, text="What is Your lastname?", bg="white", fg="black",
                         font=("Times New Roman", 12))
SFPSQuesLabel.place(x=240, y=80, anchor=tk.CENTER)
SFPSAnsEntry = tk.Entry(staffForgotPasswordFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
SFPSAnsEntry.place(x=240, y=120, anchor=tk.CENTER)
SFPSubmitButton = tk.Button(staffForgotPasswordFrame, text="Submit", fg="black", bg="white", bd=0, cursor="hand2",
                            font=("Times New Roman", 12), command=staffForgotPasswordSubmitFunction)
SFPSubmitButton.bind("<Return>", staffForgotPasswordSubmitFunction)
SFPSubmitButton.place(x=240, y=160, anchor=tk.CENTER)
SFPBackButton = tk.Button(staffForgotPasswordFrame, text="Back", bg="white", fg="black", font=("Times New Roman", 12),
                          bd=0, cursor="hand2", command=staffForgotPasswordBackFunction)
SFPBackButton.bind("<Return>", staffForgotPasswordBackFunction)
SFPBackButton.place(x=240, y=200, anchor=tk.CENTER)

# Staff Password Reset Frame
staffPasswordResetFrame = tk.LabelFrame(root, text="Reset Password", bg="white", fg="#83aff7", height=600, width=500,
                                        font=("Times New Roman", 20, "bold"))
SPRPasswordLabel = tk.Label(staffPasswordResetFrame, text="Enter the password below", bg="white", fg="black",
                            font=("Times New Roman", 12))
SPRPasswordLabel.place(x=240, y=80, anchor=tk.CENTER)
SPRPasswordEntry1 = tk.Entry(staffPasswordResetFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                             bg="white")
SPRPasswordEntry1.place(x=240, y=120, anchor=tk.CENTER)
SPRPasswordEntry2 = tk.Entry(staffPasswordResetFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED,
                             bg="white")
SPRPasswordEntry2.place(x=240, y=160, anchor=tk.CENTER)
SPRConfirmButton = tk.Button(staffPasswordResetFrame, text="Confirm", bg="white", fg="black", bd=0, cursor="hand2",
                             font=("Times New Roman", 12), command=staffResetPasswordConfirmFunction)
SPRConfirmButton.bind("<Return>", staffResetPasswordConfirmFunction)
SPRConfirmButton.place(x=240, y=200, anchor=tk.CENTER)
SPRBackButton = tk.Button(staffPasswordResetFrame, text="Back", bg="white", fg="black", bd=0, cursor="hand2",
                          font=("Times New Roman", 12), command=staffResetPasswordBackFunction)
SPRBackButton.bind("<Return>", staffResetPasswordBackFunction)
SPRBackButton.place(x=240, y=240, anchor=tk.CENTER)

# Staff Inside Login Frame
staffInsideLoginFrame = tk.LabelFrame(root, text="Data Manipulation", bg="white", fg="#83aff7", height=700, width=1200,
                                      font=("Times New Roman", 20, "bold"))
sILInfoLabel = tk.Label(staffInsideLoginFrame, text="", bg="white", fg="black", font=("Times New Roman", 15))
sILInfoLabel.place(x=600, y=30, anchor=tk.CENTER)
sILQuestionLabel = tk.Label(staffInsideLoginFrame, text="Question", bg="white", fg="black",
                            font=("Times New Roman", 12))
sILQuestionLabel.place(x=100, y=120, anchor=tk.CENTER)
sILQuestionEntry = tk.Entry(staffInsideLoginFrame, width=50, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
sILQuestionEntry.place(x=380, y=120, anchor=tk.CENTER)
sILOption1Label = tk.Label(staffInsideLoginFrame, text="Option1", bg="white", fg="black", font=("Times New Roman", 12))
sILOption1Label.place(x=100, y=160, anchor=tk.CENTER)
sILOption1Entry = tk.Entry(staffInsideLoginFrame, width=30, bg="white", relief=tk.RAISED, font=("Times New Roman", 12))
sILOption1Entry.place(x=300, y=160, anchor=tk.CENTER)
sILOption2Label = tk.Label(staffInsideLoginFrame, text="Option2", bg="white", fg="black", font=("Times New Roman", 12))
sILOption2Label.place(x=100, y=200, anchor=tk.CENTER)
sILOption2Entry = tk.Entry(staffInsideLoginFrame, width=30, bg="white", relief=tk.RAISED, font=("Times New Roman", 12))
sILOption2Entry.place(x=300, y=200, anchor=tk.CENTER)
sILOption3Label = tk.Label(staffInsideLoginFrame, text="Option3", bg="white", fg="black", font=("Times New Roman", 12))
sILOption3Label.place(x=100, y=240, anchor=tk.CENTER)
sILOption3Entry = tk.Entry(staffInsideLoginFrame, width=30, bg="white", relief=tk.RAISED, font=("Times New Roman", 12))
sILOption3Entry.place(x=300, y=240, anchor=tk.CENTER)
sILOption4Label = tk.Label(staffInsideLoginFrame, text="Option4", bg="white", fg="black", font=("Times New Roman", 12))
sILOption4Label.place(x=100, y=280, anchor=tk.CENTER)
sILOption4Entry = tk.Entry(staffInsideLoginFrame, width=30, bg="white", relief=tk.RAISED, font=("Times New Roman", 12))
sILOption4Entry.place(x=300, y=280, anchor=tk.CENTER)
sILAnswerLabel = tk.Label(staffInsideLoginFrame, text="Answer", bg="white", fg="black", font=("Times New Roman", 12))
sILAnswerLabel.place(x=100, y=320, anchor=tk.CENTER)
sILAnswerEntry = tk.Entry(staffInsideLoginFrame, width=30, bg="white", relief=tk.RAISED, font=("Times New Roman", 12))
sILAnswerEntry.place(x=300, y=320, anchor=tk.CENTER)
sILAddButton = tk.Button(staffInsideLoginFrame, text="Add", bg="white", fg="green", bd=0, font=("Times New Roman", 12),
                         cursor="hand2", command=staffInsideLoginAddFunction)
sILAddButton.bind("<Return>", staffInsideLoginAddFunction)
sILAddButton.place(x=100, y=360, anchor=tk.CENTER)
sILUpdateButton = tk.Button(staffInsideLoginFrame, text="Update", bg="white", fg="blue", bd=0,
                            font=("Times New Roman", 12), cursor="hand2", command=staffInsideLoginUpdateFunction)
sILUpdateButton.bind("<Return>", staffInsideLoginUpdateFunction)
sILUpdateButton.place(x=200, y=360, anchor=tk.CENTER)
sILDeleteButton = tk.Button(staffInsideLoginFrame, text="Delete", bg="white", fg="red", bd=0,
                            font=("Times New Roman", 12), cursor="hand2", command=staffInsideLoginDeleteFunction)
sILDeleteButton.bind("<Return>", staffInsideLoginDeleteFunction)
sILDeleteButton.place(x=300, y=360, anchor=tk.CENTER)
sILShowAllButton = tk.Button(staffInsideLoginFrame, text="Show All", bg="white", fg="Purple", bd=0,
                             font=("Times New Roman", 12), cursor="hand2", command=staffInsideLoginShowAllFunction)
sILShowAllButton.bind("<Return>", staffInsideLoginShowAllFunction)
sILShowAllButton.place(x=400, y=360, anchor=tk.CENTER)
sILNoteLabel = tk.Label(staffInsideLoginFrame, text="", bg="white", fg="#f76565", font=("Times New Roman", 12), justify=tk.LEFT)
sILNoteLabel.place(x=0, y=440)
sILLogoutButton = tk.Button(staffInsideLoginFrame, text="Log out", bg="white", fg="black", bd=0,
                            font=("Times New Roman", 12), cursor="hand2", command=staffInsideLogoutFunction)
sILLogoutButton.bind("<Return>", staffInsideLogoutFunction)
sILLogoutButton.place(x=1150, y=5, anchor=tk.CENTER)

# Student Inside Login Frame

studentInsideLoginFrame = tk.LabelFrame(root, text="Quiz", bg="white", fg="#83aff7", height=700, width=1200,
                                        font=("Times New Roman", 20, "bold"))
studentILInfoLabel = tk.Label(studentInsideLoginFrame, text="", bg="white", fg="black", font=("Times New Roman", 15))
studentILInfoLabel.place(x=600, y=10, anchor=tk.CENTER)
studentILSubjectLabel = tk.Label(studentInsideLoginFrame, text="Subject", bg="white", fg="black",
                                 font=("Times New Roman", 15))
studentILSubjectLabel.place(x=50, y=30, anchor=tk.CENTER)
studentILSubjectCombobox = ttk.Combobox(studentInsideLoginFrame, width=30, state="readonly",
                                        font=("Times New Roman", 12))
studentILSubjectCombobox.place(x=150, y=70, anchor=tk.CENTER)
studentILSubjectOkButton = tk.Button(studentInsideLoginFrame, text="Ok", bg="white", fg="black", bd=0, cursor="hand2",
                                     font=("Times New Roman", 12), command=studentInsideLoginOkFunction)
studentILSubjectOkButton.bind("<Return>", studentInsideLoginOkFunction)
studentILSubjectOkButton.place(x=320, y=70, anchor=tk.CENTER)
studentILSubmitButton = tk.Button(studentInsideLoginFrame, text="Submit", bg="white", fg="black", bd=0, cursor="hand2",
                                  font=("Times New Roman", 12), command=studentInsideSubmitFunction)
studentILSubmitButton.bind("<Return>", studentInsideSubmitFunction)
studentILLogoutButton = tk.Button(studentInsideLoginFrame, text="Log out", bg="white", fg="black", bd=0,
                                  font=("Times New Roman", 12), cursor="hand2", command=studentInsideLogoutFunction)
studentILLogoutButton.bind("<Return>", studentInsideLogoutFunction)
studentILLogoutButton.place(x=1150, y=5, anchor=tk.CENTER)

# Student Inside Login Question Frame

studentInsideLoginQuestionFrame = tk.LabelFrame(studentInsideLoginFrame, text="Question", bg="white", fg="#83aaf7",
                                                height=500, width=700, font=("Times New Roman", 15))
studentILPresentQuestionLabel = tk.Label(studentInsideLoginQuestionFrame, text="", bg="white", fg="black",
                                         font=("Times New Roman", 12))
studentILNextButton = tk.Button(studentInsideLoginQuestionFrame, text="Next >>", bg="white", fg="black", bd=0,
                                font=("Times New Roman", 12), cursor="hand2", command=studentInsideLoginNextFunction)
studentILNextButton.bind("<Return>", studentInsideLoginNextFunction)
studentILNextButton.place(x=633, y=445)
studentILPreviousButton = tk.Button(studentInsideLoginQuestionFrame, text="<< Previous", bg="white", fg="black", bd=0,
                                    font=("Times New Roman", 12), cursor="hand2",
                                    command=studentInsideLoginPreviousFunction)
studentILPreviousButton.bind("<Return>", studentInsideLoginPreviousFunction)
studentILPreviousButton.place(x=0, y=445)
variable = tk.StringVar(studentInsideLoginQuestionFrame, "0")
studentILRadioButton1 = tk.Radiobutton(studentInsideLoginQuestionFrame, variable=variable, value=1, padx=0, pady=0,
                                       text="", bg="white", cursor="hand2")
studentILRadioButton1.place(x=0, y=120)
studentILRadioButton2 = tk.Radiobutton(studentInsideLoginQuestionFrame, variable=variable, value=2, padx=0, pady=0,
                                       text="", bg="white", cursor="hand2")
studentILRadioButton2.place(x=0, y=200)
studentILRadioButton3 = tk.Radiobutton(studentInsideLoginQuestionFrame, variable=variable, value=3, padx=0, pady=0,
                                       text="", bg="white", cursor="hand2")
studentILRadioButton3.place(x=0, y=280)
studentILRadioButton4 = tk.Radiobutton(studentInsideLoginQuestionFrame, variable=variable, value=4, padx=0, pady=0,
                                       text="", bg="white", cursor="hand2")
studentILRadioButton4.place(x=0, y=360)
studentILClearButton = tk.Button(studentInsideLoginQuestionFrame, text="Clear", bg="white", fg="black", bd=0,
                                 font=("Times New Roman", 12), cursor="hand2", command=studentInsideLoginClearFunction)
studentILClearButton.bind("<Return>", studentInsideLoginClearFunction)
studentILClearButton.place(x=460, y=445)
studentILSaveButton = tk.Button(studentInsideLoginQuestionFrame, text="Save", bg="white", fg="black", bd=0,
                                font=("Times New Roman", 12), cursor="hand2", command=studentInsideLoginSaveFunction)
studentILSaveButton.bind("<Return>", studentInsideLoginSaveFunction)
studentILSaveButton.place(x=560, y=445)
root.mainloop()
