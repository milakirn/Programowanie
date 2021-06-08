from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("720x480")

lbl = Label(window, text="Hello", font=("Arial Bold", 25))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10, font=("Arial Bold", 25))
txt.grid(column=1, row=0)
txt.focus()

combo = Combobox(window, font=("Arial Bold", 25))
combo['values'] = (1, 2, 3, 4, 5, "Tekst")
combo.current(0)
combo.grid(column=1, row=1)


def clicked1():
    res = "Wpisałeś: " + txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked1)
btn.grid(column=2, row=0)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="Wybierz!")
chk.grid(column=0, row=2)

selected = IntVar()
rad1 = Radiobutton(window, text="First", value=1, variable=selected)
rad2 = Radiobutton(window, text="Second", value=2, variable=selected)
rad3 = Radiobutton(window, text="Third", value=3, variable=selected)


def clicked2():
    print(selected.get())


btn2= Button(window, text="Kliknij!", command=clicked2)
rad1.grid(column=0, row=3)
rad2.grid(column=0, row=4)
rad3.grid(column=0, row=5)
btn2.grid(column=1, row=5)

text_area = scrolledtext.ScrolledText(window, width=40, height=10)
text_area.insert(INSERT, 'GUI to moja pasja')
text_area.grid(column=0, row=6)

window.mainloop()
