import tkinter as tk
from tkinter import ttk
import time
import threading
import winsound


def submitButtonFunction():
    submitButton["state"] = tk.DISABLED
    Hours = hours.get().zfill(2)
    Minutes = mins.get().zfill(2)
    alarmTime = str(Hours) + ":" + str(Minutes)
    currentTime = time.strftime("%H:%M")
    while alarmTime != currentTime:
        currentTime = time.strftime("%H:%M")
        time.sleep(1)
    if alarmTime == currentTime:
        for i in range(5):
            winsound.Beep(2000, 700)
        root.quit()
    return


def threadProcess():
    thread = threading.Thread(target=submitButtonFunction)
    thread.start()


root = tk.Tk()
root.geometry("350x200")
root.minsize(350, 200)
root.maxsize(350, 200)
root.title("Alarm Clock")
root.iconbitmap("AlarmClockIcon.ico")
hoursLabel = tk.Label(root, text="Hours")
hours = ttk.Combobox(root, width=10, state="readonly")
hours["values"] = tuple(range(0, 24))
hours.current(0)
hours.place(x=140, y=60, anchor=tk.CENTER)
hoursLabel.place(x=140, y=40, anchor=tk.CENTER)
minsLabel = tk.Label(root, text="Minutes")
mins = ttk.Combobox(root, width=10, state="readonly")
mins["values"] = tuple(range(0, 60))
mins.current(0)
mins.place(x=210, y=60, anchor=tk.CENTER)
minsLabel.place(x=210, y=40, anchor=tk.CENTER)
submitButton = tk.Button(root, text="Submit", command=threadProcess)
submitButton.place(x=175, y=100, anchor=tk.CENTER)
root.mainloop()
