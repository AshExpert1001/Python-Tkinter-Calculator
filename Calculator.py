from tkinter import *

def click(event):
    global _value
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if _value.get().isdigit():
            value = int(_value.get())
        else:
            try:
                value = eval(Screen.get())

            except Exception as e:
                print(e)
                value = "Equation Error!"

        _value.set(value)
        Screen.update()

    elif text == "c":
        _value.set("")
        Screen.update()

    else:
        _value.set(_value.get() + text)
        Screen.update()

root = Tk()
root.geometry("280x360")
root.minsize(280, 360)
root.maxsize(280, 360)
root.title("AshExpert Calculator")
root.config(background="#d3d3d3")
root.wm_iconbitmap("icon/icon.ico")

_value = StringVar()
_value.set("")

Screen = Entry(root, textvar=_value, font="lucida 20 bold")
Screen.pack(fill=X, ipady=18)

frame =Frame(root, bg="#d3d3d3", pady=10)
btn = Button(frame, text="9", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="8", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="7", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="=", padx=14, pady=10, bg="#7dea7e", fg="#fff", font="lucida 12 bold")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
frame.pack()

frame =Frame(root, bg="#d3d3d3", pady=10)
btn = Button(frame, text="6", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="5", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="4", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="/", padx=14, pady=10, bg="#b1b1b1", fg="#fff", font="lucida 12 bold")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
frame.pack()

frame =Frame(root, bg="#d3d3d3", pady=10)
btn = Button(frame, text="3", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="2", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="1", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="*", padx=14, pady=10, bg="#b1b1b1", fg="#fff", font="lucida 12 bold")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
frame.pack()

frame =Frame(root, bg="#d3d3d3", pady=10)
btn = Button(frame, text="c", padx=14, pady=10, bg="#ff6060", fg="#fff", font="lucida 12 bold")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="0", padx=14, pady=10, font="lucida 12 italic")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="-", padx=14, pady=10, bg="#b1b1b1", fg="#fff", font="lucida 12 bold")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
btn = Button(frame, text="+", padx=14, pady=10, bg="#b1b1b1", fg="#fff", font="lucida 12 bold")
btn.pack(side=LEFT, padx=10)
btn.bind('<Button-1>', click)
frame.pack()

root.mainloop()