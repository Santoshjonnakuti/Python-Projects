from tkinter import *
global operator
global first
global final


def click(number):
    global final
    initial = e.get()
    e.delete(0, END)
    final = str(initial) + str(number)
    e.insert(0, final)
    return


def add():
    global operator
    global first
    operator = "add"
    first = float(e.get())
    e.delete(0, END)


def sub():
    global operator
    global first
    operator = "sub"
    first = float(e.get())
    e.delete(0, END)


def mul():
    global operator
    global first
    operator = "mul"
    first = float(e.get())
    e.delete(0, END)


def div():
    global operator
    global first
    operator = "div"
    first = float(e.get())
    e.delete(0, END)


def per():
    number = float(e.get())
    e.delete(0, END)
    number = number/100
    e.insert(0, number)


def equal():
    global final
    second = float(e.get())
    e.delete(0, END)
    op = operator
    if op == "add":
        final = str(float(first) + float(second))
    elif op == 'sub':
        final = str(float(first) - float(second))
    elif op == 'mul':
        final = str(float(first) * float(second))
    elif op == 'div':
        if float(second) == 0:
            final = "Syntax Error"
        else:
            final = str(float(first) / float(second))
    e.insert(0, final)


def clear():
    e.delete(0, END)


root = Tk()
root.title("Calculator")
e = Entry(root, width=30, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button1 = Button(root, text="1", padx=20, pady=10, command=lambda: click(1))
button2 = Button(root, text="2", padx=20, pady=10, command=lambda: click(2))
button3 = Button(root, text="3", padx=20, pady=10, command=lambda: click(3))
button4 = Button(root, text="4", padx=20, pady=10, command=lambda: click(4))
button5 = Button(root, text="5", padx=20, pady=10, command=lambda: click(5))
button6 = Button(root, text="6", padx=20, pady=10, command=lambda: click(6))
button7 = Button(root, text="7", padx=20, pady=10, command=lambda: click(7))
button8 = Button(root, text="8", padx=20, pady=10, command=lambda: click(8))
button9 = Button(root, text="9", padx=20, pady=10, command=lambda: click(9))
button0 = Button(root, text="0", padx=20, pady=10, command=lambda: click(0))
button_add = Button(root, text="+", padx=19, pady=10, command=add)
button_sub = Button(root, text="-", padx=20, pady=10, command=sub)
button_mul = Button(root, text="*", padx=20, pady=10, command=mul)
button_div = Button(root, text="/", padx=20, pady=10, command=div)
button_per = Button(root, text="%", padx=20, pady=10, command=per)
button_clear = Button(root, text="C", padx=19, pady=10, command=clear)
button_equal = Button(root, text="=", padx=19, pady=10, command=equal)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

root.mainloop()
