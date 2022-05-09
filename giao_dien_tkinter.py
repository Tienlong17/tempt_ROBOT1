from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import *
import tkinter
import tempt 

window = Tk()
window.title("Quaruped")
window.geometry("800x600")

# Thêm label
lbl = tkinter.Label(window, text ="Quaruped Robot", fg="red", font=("Arial", 20))
lbl.grid(column=0, row=0)

# Thêm textbox
txt = Entry(window, width=20)
txt.grid(column=0, row=1)

# chuc nang item thuc hien ham, phải viết trước event button
def handleButton():
    lbl.configure(text = "Hi," + txt.get())
    return

# Thêm button
btnHello = Button(window, text="Say Hello", command=handleButton)
btnHello.grid(column=1, row=1)

# Thêm combobox

combo = Combobox(window)
combo['values'] = ("Trotting", "Bạn 2", "Bạn 3")
combo.current(0)
combo.grid(column=0, row=2 )


def handleButton1():
    #lbl.configure(text = "Hi," + combo.get())
    messagebox.showinfo("Mì AI Test", "Hi," + combo.get())
    return

# Thêm button
btnHello1 = Button(window, text="Say Hello Combo", command=handleButton1)
btnHello1.grid(column=1, row=2)

# hàm chức năng di chuyển
def Go_up():
    tempt.xinchao()
    handleButton1()
#them button di chuyển
btnUp = Button(window, text="Up", command=tempt.xinchao())
btnUp.grid(column=5, row=1)

btnDown = Button(window, text="Down", command=tempt.xinchao())
btnDown.grid(column=5, row=3)

btnStop = Button(window, text="Stop", command=tempt.xinchao())
btnStop.grid(column=5, row=2)

btnLeft = Button(window, text="Left", command=tempt.xinchao())
btnLeft.grid(column=4, row=2)

btnRight = Button(window, text="Left", command=tempt.xinchao())
btnRight.grid(column=6, row=2)

window.mainloop()