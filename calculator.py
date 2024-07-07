from tkinter import *
import tkinter as tk

def click(event):
    global input1
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if input1.get().isdigit():
            value = int(input1.get())
        else:
            try:
               value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
                screen.update()

        input1.set(value)
        screen.update()

    elif text == "C":
        input1.set("")
        screen.update()

    else:
        input1.set(input1.get() + text)
        screen.update()

root = Tk()
root.geometry("400x700")
root.title("Calculator")
root.wm_iconbitmap("icon.ico")
root.configure(bg="white")

def lightMode():
    root.configure(bg="white" )
    screen.configure(bg="white", fg="black")
    for button in [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonEqual, buttondivide, buttonmultiply, buttonminus, buttonplus, buttonC]:
       button.configure(bg="white", fg="black")

def darkMode():
    root.configure(bg="black" )
    screen.configure(bg="black", fg="white")
    for button in [button0, button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonEqual, buttondivide, buttonmultiply, buttonminus, buttonplus, buttonC]:
       button.configure(bg="black", fg="white")

def about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("250x150")

    about_label = tk.Label(about_window, text="Made By Haris - All rights reserverd 2024", justify=tk.LEFT)
    about_label.pack(pady=10, padx=10)

    ok_button = tk.Button(about_window, text="OK", command=about_window.destroy)
    ok_button.pack(pady=5)


menubar = tk.Menu(root)
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Dark Mode", command=darkMode)
helpmenu.add_command(label="Light Mode", command=lightMode)
menubar.add_cascade(label="More", menu=helpmenu)
root.config(menu=menubar)
root.configure(bg="white")

input1 = StringVar()
input1.set("")
screen = Entry(root, textvariable= input1, font="lucida 40 bold")
screen.pack(fill = X, padx = 10, pady = 10, ipadx = 10, ipady = 10)
screen.configure(bg="white", fg = "black")


frame1 = Frame(root, bg="white")
button9 = Button(frame1, text="9",padx = 10, pady = 10, font = "lucida 40 bold")
button9.pack(side = LEFT, padx = 5, pady =5)
button9.bind("<Button-1>", click)

button8 = Button(frame1, text="8", padx = 10, pady = 10, font = "lucida 40 bold")
button8.pack(side = LEFT, padx = 5, pady =5)
button8.bind("<Button-1>", click)

button7 = Button(frame1, text="7", padx = 10, pady = 10, font = "lucida 40 bold")
button7.pack(side = LEFT, padx = 5, pady =5)
button7.bind("<Button-1>", click)

buttonplus = Button(frame1, text="+", padx = 10, pady = 10, font = "lucida 40 bold")
buttonplus.pack(side = LEFT, padx = 5, pady =5)
buttonplus.bind("<Button-1>", click)
frame1.pack()

frame2 = Frame(root, bg="white")
button6 = Button(frame2, text="6", padx = 10, pady = 10, font = "lucida 40 bold")
button6.pack(side = LEFT, padx = 5, pady =5)
button6.bind("<Button-1>", click)

button5 = Button(frame2, text="5", padx = 10, pady = 10, font = "lucida 40 bold")
button5.pack(side = LEFT, padx = 5, pady =5)
button5.bind("<Button-1>", click)

button4 = Button(frame2, text="4", padx = 10, pady = 10, font = "lucida 40 bold")
button4.pack(side = LEFT, padx = 5, pady =5)
button4.bind("<Button-1>", click)

buttonminus = Button(frame2, text="-", padx = 10, pady = 10, font = "lucida 40 bold")
buttonminus.pack(side = LEFT, padx = 5, pady =5)
buttonminus.bind("<Button-1>", click)

frame2.pack()

frame3 = Frame(root, bg="white")
button3 = Button(frame3, text="3", padx = 10, pady = 10, font = "lucida 40 bold")
button3.pack(side = LEFT, padx = 5, pady =5)
button3.bind("<Button-1>", click)

button2 = Button(frame3, text="2", padx = 10, pady = 10, font = "lucida 40 bold")
button2.pack(side = LEFT, padx = 5, pady =5)
button2.bind("<Button-1>", click)

button1 = Button(frame3, text="1", padx = 10, pady = 10, font = "lucida 40 bold")
button1.pack(side = LEFT, padx = 5, pady =5)
button1.bind("<Button-1>", click)

buttonmultiply = Button(frame3, text="*", padx = 10, pady = 10, font = "lucida 40 bold")
buttonmultiply.pack(side = LEFT, padx = 5, pady =5)
buttonmultiply.bind("<Button-1>", click)

frame3.pack()

frame5 = Frame(root, bg="white")
buttonEqual = Button(frame5, text = "=", padx = 10, pady = 10, font = "lucida 40 bold")
buttonEqual.pack(side = LEFT, padx = 5, pady =5)
buttonEqual.bind("<Button-1>", click)


button0 = Button(frame5, text="0", padx = 10, pady = 10, font = "lucida 40 bold")
button0.pack(side = LEFT, padx = 5, pady =5)
button0.bind("<Button-1>", click)

buttondivide = Button(frame5, text="/", padx = 10, pady = 10, font = "lucida 40 bold")
buttondivide.pack(side = LEFT, padx = 5, pady =5)
buttondivide.bind("<Button-1>", click)

buttonC = Button(frame5, text = "C", padx = 10, pady = 10, font = "lucida 40 bold")
buttonC.pack(side = LEFT, padx = 5, pady =5)
buttonC.bind("<Button-1>", click)



frame5.pack()

root.mainloop()