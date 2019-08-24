
import tkinter as tk
from tkinter import StringVar
import math

win = tk.Tk()
win.title("Calculator")
win.resizable(False, False)
xPos = int(win.winfo_screenwidth()/2 - win.winfo_reqwidth())
yPos = int(win.winfo_screenheight()/2 - win.winfo_reqheight())
win.geometry("+{}+{}".format(xPos, yPos))
win.geometry("347x570")


win.config(bg="gray25")
#win.attributes("-transparentcolor", "dodger blue")

res = StringVar()
vara = StringVar()
varb = StringVar()
save = StringVar()
save2 = StringVar()

entrya = tk.Entry(win,  width=20, textvariable = vara, bg="bisque", justify = tk.CENTER, font = ('courier', 24, 'bold'))
entrya.place(x=231, y=10, width=100, height=80)

entryb = tk.Entry(win, width=20, textvariable = varb, bg="bisque", justify = tk.CENTER, font = ('courier', 24, 'bold'))
entryb.place(x=231, y=95, width=100, height=80)

entryres = tk.Label(win, text="RESULT", textvariable = res, relief="solid", font=("Courier",25,'bold'), anchor='w')
entryres.place(x=16, y=185, width=315, height=80)

saveVal = tk.Label(win, text="SAVE", textvariable = save, font=("Courier",20,'bold'), anchor='w')
saveVal.place(x=16, y=130, width = 100)

#saveVal2 = tk.Label(win, text="SAVE", textvariable = save2, font=("Courier",30,'bold'), anchor='e')
#saveVal2.place(x=231, y=130, width = 100)


def add(entrya, entryb, res):
    aval = entrya.get()
    bval = entryb.get()
    try:
        b = int(bval)
        a = int(aval)
    except ValueError:
        return False
    res.set(a + b)
    
def diff(entrya, entryb, entryres):
    aval = entrya.get()
    bval = entryb.get()
    try:
        b = int(bval)
        a = int(aval)
    except ValueError:
        return False
    res.set(a - b)

def multiply(entrya, entryb, entryres):
    aval = entrya.get()
    bval = entryb.get()
    try:
        b = int(bval)
        a = int(aval)
    except ValueError:
        return False
    res.set(a * b)

def divide(entrya, entryb, entryres):
    aval = entrya.get()
    bval = entryb.get()
    try:
        b = int(bval)
        a = int(aval)
    except ValueError:
        return False
    res.set(float(a / b))

def square(entrya, entryres):
    if vara.get() != "":
        aval = entrya.get()
        try:
            a = int(aval)
        except ValueError:
            return False
        save.set(a)
        res.set(int(save.get()) * int(save.get()))
        vara.set("")
        return
    else:
        resval = res.get()
        try:
            r = int(resval)
        except ValueError:
            return False
        save.set(r)
        res.set(int(save.get()) * int(save.get()))
        
    
def squareRoot(entrya, entryres):
    if vara.get() != "":
        sqr = math.sqrt(float(vara.get()))
        strsqr = str(sqr)
        if strsqr[len(strsqr)-1] == '0' and strsqr[len(strsqr)-2] == '.':
            res.set(int(sqr))
        else:
            res.set(sqr)
        vara.set("")
        return
    else:
        sqr = math.sqrt(float(res.get()))
        strsqr = str(sqr)
        if strsqr[len(strsqr)-1] == '0' and strsqr[len(strsqr)-2] == '.':
            res.set(int(sqr))
        else:
            res.set(sqr)

tk.Button(win, text="+", font=("arial", 20, "bold"), bg="salmon3", width=5, height=3, command = lambda: add(entrya, entryb, res)).place(x=16, y=282)
tk.Button(win, text="-", font=("arial", 20, "bold"), bg="salmon3", width=5, height=3, command = lambda: diff(entrya, entryb, entryres)).place(x=16, y=421)
tk.Button(win, text="X", font=("arial", 20, "bold"), bg="salmon3", width=5, height=3, command = lambda: multiply(entrya, entryb, entryres)).place(x=121, y=282)
tk.Button(win, text="/", font=("arial", 20, "bold"), bg="salmon3", width=5, height=3, command = lambda: divide(entrya, entryb, entryres)).place(x=121, y=421)
tk.Button(win, text="^2", font=("arial", 20, "bold"), bg="dark slate blue", width=5, height=3, command = lambda: square(entrya, entryres)).place(x= 226, y=282)
tk.Button(win, text="√", font=("arial", 20, "bold"), bg="dark slate blue", width=5, height=3, command = lambda: squareRoot(entrya, entryres)).place(x=226, y=421)
win.mainloop()
