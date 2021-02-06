import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import StudentDataBase
import StaffDataBase


def studentShowPasswordFunction():
    if studentShowPasswordButton["text"] == "Show Password":
        studentShowPasswordButton.config(text="Hide Password")
        studentPasswordEntry.config(show="")
    else:
        studentShowPasswordButton.config(text="Show Password")
        studentPasswordEntry.config(show="*")
    return


def studentSignUpFunction():
    studentLoginFrame.place_forget()
    staffLoginFrame.place_forget()
    studentSignUpFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def studentLoginFunction():
    username = studentUsernameEntry.get()
    password = studentPasswordEntry.get()
    if username == "" or username is None:
        messagebox.showwarning("Warning", "Username Cannot be empty...")
    elif password == "" or password is None:
        messagebox.showwarning("Warning", "Password Cannot be empty...")
    else:
        pwd = StudentDataBase.getStudent(username)
        if pwd == password:
            studentLoginFrame.place_forget()
            staffLoginFrame.place_forget()
        elif pwd is None:
            messagebox.showerror("Error", "Student not found...")
        elif pwd != password:
            messagebox.showerror("Error", "Incorrect Password")
        pass
    return


def StudentSignUpFunction():
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


def studentSignUpBackFunction():
    studentSignUpFrame.place_forget()
    studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)
    staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)
    return


def staffShowPasswordFunction():
    if staffShowPasswordButton["text"] == "Show Password":
        staffShowPasswordButton.config(text="Hide Password")
        staffPasswordEntry.config(show="")
    else:
        staffShowPasswordButton.config(text="Show Password")
        staffPasswordEntry.config(show="*")
    return


def staffSignUpFunction():
    studentLoginFrame.place_forget()
    staffLoginFrame.place_forget()
    staffSignUpFrame.place(x=700, y=400, anchor=tk.CENTER)
    return


def staffLoginFunction():
    username = staffUsernameEntry.get()
    password = staffPasswordEntry.get()
    if username == "" or username is None:
        messagebox.showwarning("Warning", "Username Cannot be empty...")
    elif password == "" or password is None:
        messagebox.showwarning("Warning", "Password Cannot be empty...")
    else:
        pwd = StaffDataBase.getStaff(username)
        if pwd == password:
            studentLoginFrame.place_forget()
            staffLoginFrame.place_forget()
        elif pwd is None:
            messagebox.showerror("Error", "Staff not found...")
        elif pwd != password:
            messagebox.showerror("Error", "Incorrect Password")
    return


def StaffSignUpFunction():
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
    messagebox.showinfo("Info", "Successfully Registered...")
    return


def staffSignUpBackFunction():
    staffSignUpFrame.place_forget()
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
studentLoginFrame = tk.LabelFrame(root, text="Student Login", bg="white", fg="#83aff7", height=600, width=500, font=("Times New Roman", 20, "bold"))
studentLoginFrame.place(x=400, y=400, anchor=tk.CENTER)

studentUsernameLabel = tk.Label(studentLoginFrame, text="Username", bg="white", fg="#43518c", font=("Times New Roman", 15, "bold"))
studentUsernameLabel.place(x=50, y=40, anchor=tk.CENTER)
studentUsernameEntry = tk.Entry(studentLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED)
studentUsernameEntry.place(x=170, y=80, anchor=tk.CENTER)
studentPasswordLabel = tk.Label(studentLoginFrame, text="Password", bg="white", fg="#43518c", font=("Times New Roman", 15, "bold"))
studentPasswordLabel.place(x=50, y=120, anchor=tk.CENTER)
studentPasswordEntry = tk.Entry(studentLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED, show="*")
studentPasswordEntry.place(x=170, y=160, anchor=tk.CENTER)
studentShowPasswordButton = tk.Button(studentLoginFrame, text="Show Password", bg="white", fg="black", bd=0, font=("Times New Roman", 10), cursor="hand2", command=studentShowPasswordFunction)
studentShowPasswordButton.place(x=400, y=160, anchor=tk.CENTER)
studentForgotPasswordButton = tk.Button(studentLoginFrame, text="Forgot Password?", bg="white", fg="#453c85", bd=0, font=("Times New Roman", 10), cursor="hand2")
studentForgotPasswordButton.place(x=285, y=190, anchor=tk.CENTER)
studentLoginButton = tk.Button(studentLoginFrame, text="Log In", bg="white", fg="#4b396e", font=("Times New Roman", 12), cursor="hand2", bd=0, command=studentLoginFunction)
studentLoginButton.place(x=30, y=220, anchor=tk.CENTER)
studentSignUpButton = tk.Button(studentLoginFrame, text="Don't have an account? Sign up", bg="white", fg="#4b396e", bd=0, cursor="hand2", font=("Times New Roman", 10), command=studentSignUpFunction)
studentSignUpButton.place(x=95, y=260, anchor=tk.CENTER)


# Staff Login Frame
staffLoginFrame = tk.LabelFrame(root, text="Staff Login", bg="white", fg="#83aff7", height=600, width=500, font=("Times New Roman", 20, "bold"))
staffLoginFrame.place(x=1100, y=400, anchor=tk.CENTER)

staffUsernameLabel = tk.Label(staffLoginFrame, text="Username", bg="white", fg="#43518c", font=("Times New Roman", 15, "bold"))
staffUsernameLabel.place(x=50, y=40, anchor=tk.CENTER)
staffUsernameEntry = tk.Entry(staffLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED)
staffUsernameEntry.place(x=170, y=80, anchor=tk.CENTER)
staffPasswordLabel = tk.Label(staffLoginFrame, text="Password", bg="white", fg="#43518c", font=("Times New Roman", 15, "bold"))
staffPasswordLabel.place(x=50, y=120, anchor=tk.CENTER)
staffPasswordEntry = tk.Entry(staffLoginFrame, width=40, font=("Times New Roman", 12), bg="white", relief=tk.RAISED, show="*")
staffPasswordEntry.place(x=170, y=160, anchor=tk.CENTER)
staffShowPasswordButton = tk.Button(staffLoginFrame, text="Show Password", bg="white", fg="black", bd=0, font=("Times New Roman", 10), cursor="hand2", command=staffShowPasswordFunction)
staffShowPasswordButton.place(x=400, y=160, anchor=tk.CENTER)
staffForgotPasswordButton = tk.Button(staffLoginFrame, text="Forgot Password?", bg="white", fg="#453c85", bd=0, font=("Times New Roman", 10), cursor="hand2")
staffForgotPasswordButton.place(x=285, y=190, anchor=tk.CENTER)
staffLoginButton = tk.Button(staffLoginFrame, text="Log In", bg="white", fg="#4b396e", font=("Times New Roman", 12), cursor="hand2", bd=0, command=staffLoginFunction)
staffLoginButton.place(x=30, y=220, anchor=tk.CENTER)
staffSignUpButton = tk.Button(staffLoginFrame, text="Don't have an account? Sign up", bg="white", fg="#4b396e", bd=0, cursor="hand2", font=("Times New Roman", 10), command=staffSignUpFunction)
staffSignUpButton.place(x=95, y=260, anchor=tk.CENTER)

# Student Sign up Frame
studentSignUpFrame = tk.LabelFrame(root, text="Sign up", bg="white", fg="#83aff7", height=600, width=500, font=("Times New Roman", 20, "bold"))
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
dateOfBirthLabel = tk.Label(studentSignUpFrame, text="Date of Birth", bg="white", fg="black", font=("Times New Roman", 12))
dateOfBirthLabel.place(x=95, y=240, anchor=tk.CENTER)
dateOfBirthEntry = DateEntry(studentSignUpFrame, width=42, bg="black", fg="white", year=2000, state="readonly")
dateOfBirthEntry.place(x=305, y=240, anchor=tk.CENTER)
securityQuestionsLabel = tk.Label(studentSignUpFrame, text="Security Question", bg="white", fg="black", font=("Times New Roman", 12))
securityQuestionsLabel.place(x=82, y=280, anchor=tk.CENTER)
securityQuestions = ttk.Combobox(studentSignUpFrame, width=30, state="readonly", font=("Times New Roman", 12))
securityQuestions["values"] = tuple(["What is your lastname?", "What is your Pet name?", "What is your nickname?"])
securityQuestions.current(0)
securityQuestions.place(x=300, y=280, anchor=tk.CENTER)
securityQuesAnsLabel = tk.Label(studentSignUpFrame, text="Answer", fg="black", bg="white", font=("Times New Roman", 12))
securityQuesAnsLabel.place(x=113, y=320, anchor=tk.CENTER)
securityQuesAnsEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
securityQuesAnsEntry.place(x=290, y=320, anchor=tk.CENTER)
passwordLabel = tk.Label(studentSignUpFrame, text="Password", bg="white", fg="black", font=("Times New Roman", 12))
passwordLabel.place(x=108, y=360, anchor=tk.CENTER)
passwordEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
passwordEntry.place(x=290, y=360, anchor=tk.CENTER)
reEntryPasswordLabel = tk.Label(studentSignUpFrame, text="Re-enter Password", bg="white", fg="black", font=("Times New Roman", 12))
reEntryPasswordLabel.place(x=80, y=400, anchor=tk.CENTER)
reEntryPasswordEntry = tk.Entry(studentSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
reEntryPasswordEntry.place(x=290, y=400, anchor=tk.CENTER)
signUpButton = tk.Button(studentSignUpFrame, text="Sign up", bg="white", fg="black", font=("Times New Roman", 12), cursor="hand2", bd=0, command=StudentSignUpFunction)
signUpButton.place(x=240, y=440, anchor=tk.CENTER)
signUpBackButton = tk.Button(studentSignUpFrame, text="Back", fg="black", bg="white", font=("Times New Roman", 12), cursor="hand2", bd=0, command=studentSignUpBackFunction)
signUpBackButton.place(x=240, y=550, anchor=tk.CENTER)

# Staff Sign up Frame
staffSignUpFrame = tk.LabelFrame(root, text="Sign up", bg="white", fg="#83aff7", height=600, width=500, font=("Times New Roman", 20, "bold"))
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
staffDateOfBirthLabel = tk.Label(staffSignUpFrame, text="Date of Birth", bg="white", fg="black", font=("Times New Roman", 12))
staffDateOfBirthLabel.place(x=95, y=240, anchor=tk.CENTER)
staffDateOfBirthEntry = DateEntry(staffSignUpFrame, width=42, bg="black", fg="white", year=2000, state="readonly")
staffDateOfBirthEntry.place(x=305, y=240, anchor=tk.CENTER)
staffSecurityQuestionsLabel = tk.Label(staffSignUpFrame, text="Security Question", bg="white", fg="black", font=("Times New Roman", 12))
staffSecurityQuestionsLabel.place(x=82, y=280, anchor=tk.CENTER)
staffSecurityQuestions = ttk.Combobox(staffSignUpFrame, width=30, state="readonly", font=("Times New Roman", 12))
staffSecurityQuestions["values"] = tuple(["What is your lastname?", "What is your Pet name?", "What is your nickname?"])
staffSecurityQuestions.current(0)
staffSecurityQuestions.place(x=300, y=280, anchor=tk.CENTER)
staffSecurityQuesAnsLabel = tk.Label(staffSignUpFrame, text="Answer", fg="black", bg="white", font=("Times New Roman", 12))
staffSecurityQuesAnsLabel.place(x=113, y=320, anchor=tk.CENTER)
staffSecurityQuesAnsEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffSecurityQuesAnsEntry.place(x=290, y=320, anchor=tk.CENTER)
stafPasswordLabel = tk.Label(staffSignUpFrame, text="Password", bg="white", fg="black", font=("Times New Roman", 12))
stafPasswordLabel.place(x=108, y=360, anchor=tk.CENTER)
stafPasswordEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
stafPasswordEntry.place(x=290, y=360, anchor=tk.CENTER)
staffReEntryPasswordLabel = tk.Label(staffSignUpFrame, text="Re-enter Password", bg="white", fg="black", font=("Times New Roman", 12))
staffReEntryPasswordLabel.place(x=80, y=400, anchor=tk.CENTER)
staffReEntryPasswordEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffReEntryPasswordEntry.place(x=290, y=400, anchor=tk.CENTER)
staffSubjectLabel = tk.Label(staffSignUpFrame, text="Subject", bg="white", fg="black", font=("Times New Roman", 12))
staffSubjectLabel.place(x=108, y=440, anchor=tk.CENTER)
staffSubjectEntry = tk.Entry(staffSignUpFrame, width=30, font=("Times New Roman", 12), relief=tk.RAISED, bg="white")
staffSubjectEntry.place(x=290, y=440, anchor=tk.CENTER)
staffSignUpButton = tk.Button(staffSignUpFrame, text="Sign up", bg="white", fg="black", font=("Times New Roman", 12), cursor="hand2", bd=0, command=StaffSignUpFunction)
staffSignUpButton.place(x=240, y=480, anchor=tk.CENTER)
staffSignUpBackButton = tk.Button(staffSignUpFrame, text="Back", fg="black", bg="white", font=("Times New Roman", 12), cursor="hand2", bd=0, command=staffSignUpBackFunction)
staffSignUpBackButton.place(x=240, y=550, anchor=tk.CENTER)

root.mainloop()
