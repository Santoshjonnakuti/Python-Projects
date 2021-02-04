from tkinter import *
from tkinter import ttk
import time
import threading
import winsound


def submitButtonFunction():
    submitButton["state"] = DISABLED
    Hours = hours.get().zfill(2)
    Minutes = mins.get().zfill(2)
    Seconds = secs.get().zfill(2)
    Minutes = int(Minutes) + (int(Hours)*60)
    Seconds = int(Seconds) + (int(Minutes)*60)
    Seconds = int(Seconds)
    time.sleep(Seconds)
    for i in range(5):
        winsound.Beep(2000, 700)
    root.quit()


def threadProcess():
    thread = threading.Thread(target=submitButtonFunction)
    thread.start()


root = Tk()
root.geometry("420x200")
root.minsize(420, 200)
root.maxsize(420, 200)
root.title("Timer")
root.iconbitmap("Timer.ico")
hoursLabel = Label(root, text="Hours")
hours = ttk.Combobox(root, width=10, state="readonly")
hours["values"] = tuple(range(0, 24))
hours.current(0)
hours.place(relx=0.3, rely=0.3, anchor=CENTER)
hoursLabel.place(relx=0.3, rely=0.20, anchor=CENTER)
minsLabel = Label(root, text="Minutes")
mins = ttk.Combobox(root, width=10, state="readonly")
mins["values"] = tuple(range(0, 60))
mins.current(0)
mins.place(relx=0.5, rely=0.3, anchor=CENTER)
minsLabel.place(relx=0.5, rely=0.20, anchor=CENTER)
secsLabel = Label(root, text="Seconds")
secs = ttk.Combobox(root, width=10, state="readonly")
secs["values"] = tuple(range(0, 60))
secs.current(0)
secs.place(relx=0.7, rely=0.3, anchor=CENTER)
secsLabel.place(relx=0.7, rely=0.2, anchor=CENTER)
submitButton = Button(root, text="Submit", command=threadProcess)
submitButton.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
