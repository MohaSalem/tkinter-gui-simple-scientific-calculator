from tkinter import *
import math
from tkinter import messagebox
from random import random
import time
from tkinter import filedialog

# Creating and adjusting the main root window
root = Tk()
root.geometry("550x266")
root.title("Calculator")
root.resizable(0, 0)

"""Creating a new log file with the time stamp for the calculator session operations"""
time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S")
file_signature = time_stamp + ".txt"
log_file = open(file_signature, "w")

# Creating a frame for the calculator menu
menuFrame = Frame(root)
menuFrame.pack(side=TOP)


def simpleCalc():
    """This method switches to the simple calculator"""
    root.geometry("550x266")


def scientificCalc():
    """This method switches to the scientific calculator"""
    root.geometry("550x333")


def about():
    """This methods shows the about info"""
    messagebox.showinfo("Info!", "Mainor Calculator Version 1.1 "
                                 "By Mohamed Salem "
                                 "©2020 EUAS")


def logs():
    log_file = filedialog.askopenfilename(initialdir="M:\gui", title="Select a log file",
                                              filetypes=(("Text files","*.txt*"),("all files","*.*")))
    with open(log_file) as data:
        print(data.read())
        messagebox.showinfo(data.read())



    # Creating and adjusting the file and help menus in the calculator menu
fileMenu = Menubutton(menuFrame, text="File", relief=GROOVE)
fileMenu.menu = Menu(fileMenu, tearoff=0)
fileMenu["menu"] = fileMenu.menu
fileMenu.menu.add_command(label="Simple Calculator", command=simpleCalc)
fileMenu.menu.add_command(label="Scientific Calculator", command=scientificCalc)
fileMenu.menu.add_command(label="Terminate Application", command=root.quit)
fileMenu.grid(column=0, row=0)
helpMenu = Menubutton(menuFrame, text="Help", relief=GROOVE)
helpMenu.menu = Menu(helpMenu, tearoff=0)
helpMenu["menu"] = helpMenu.menu
helpMenu.menu.add_command(label="View Logs", command=logs)
helpMenu.menu.add_command(label="About", command=about)
helpMenu.grid(column=1, row=0)


# Creating the button click functions
def btn1_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '1')


def btn2_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '2')


def btn3_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '3')


def btn4_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '4')


def btn5_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '5')


def btn6_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '6')


def btn7_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '7')


def btn8_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '8')


def btn9_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '9')


def btn0_clicked():
    if calculator_display.get() == '0':
        calculator_display.delete(0, END)
    place = len(calculator_display.get())
    calculator_display.insert(place, '0')


def btn_plus_clicked():
    place = len(calculator_display.get())
    calculator_display.insert(place, '+')


def btn_minus_clicked():
    place = len(calculator_display.get())
    calculator_display.insert(place, '-')


def btn_multiply_clicked():
    place = len(calculator_display.get())
    calculator_display.insert(place, '*')


def btn_divide_clicked():
    place = len(calculator_display.get())
    calculator_display.insert(place, '/')


def btn_clear_clicked():
    calculator_display.delete(0, END)
    calculator_display.insert(0, '0')


def sin_clicked():
    try:
        result = math.sin(float(calculator_display.get()))
        calculator_display.delete(0, END)
        calculator_display.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error!", "Try again!")


def cos_clicked():
    try:
        result = math.cos(float(calculator_display.get()))
        calculator_display.delete(0, END)
        calculator_display.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error!", "Try again!")


def tan_clicked():
    try:
        result = math.tan(float(calculator_display.get()))
        calculator_display.delete(0, END)
        calculator_display.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error!", "Try again!")


def rand_clicked():
    try:
        result = random()
        calculator_display.delete(0, END)
        calculator_display.insert(0, str(result))
    except Exception:
        messagebox.showerror("Error!", "Try again!")


def dot_clicked():
    place = len(calculator_display.get())
    calculator_display.insert(place, '.')


def btn_equal_clicked():
    try:
        expression = calculator_display.get()
        result = eval(expression)
        calculator_display.delete(0, END)
        calculator_display.insert(0, result)
        item = (str(expression) + " = " + str(result))
        # Writing the operations data line by line in our created file
        log_file.write(item)
        log_file.write("\n")
    except:
        messagebox.showerror("Error!", "Try again!")


# Creating and adjusting the calculator display entry
calculator_display = Entry(root, font="Verdana 20", fg="black", bg="#abbab1", bd=0, justify=RIGHT,
                           insertbackground="#abbab1")
calculator_display.insert(0, '0')
calculator_display.focus_set()
calculator_display.pack(expand=TRUE, fill=BOTH)

# Creating and adjusting the calculator buttons
row1 = Frame(root, bg="#000000")
row1.pack(expand=TRUE, fill=BOTH)
btn1 = Button(row1, text="1", font="Segoe 23", relief=GROOVE, bd=0, command=btn1_clicked, fg="white", bg="#333333")
btn1.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn2 = Button(row1, text="2", font="Segoe 23", relief=GROOVE, bd=0, command=btn2_clicked, fg="white", bg="#333333")
btn2.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn3 = Button(row1, text="3", font="Segoe 23", relief=GROOVE, bd=0, command=btn3_clicked, fg="white", bg="#333333")
btn3.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn_plus = Button(row1, text="+", font="Segoe 23", relief=GROOVE, bd=0, command=btn_plus_clicked, fg="white",
                  bg="#333333")
btn_plus.pack(side=LEFT, expand=TRUE, fill=BOTH)
row2 = Frame(root)
row2.pack(expand=TRUE, fill=BOTH)
btn4 = Button(row2, text="4", font="Segoe 23", relief=GROOVE, bd=0, command=btn4_clicked, fg="white", bg="#333333")
btn4.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn5 = Button(row2, text="5", font="Segoe 23", relief=GROOVE, bd=0, command=btn5_clicked, fg="white", bg="#333333")
btn5.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn6 = Button(row2, text="6", font="Segoe 23", relief=GROOVE, bd=0, command=btn6_clicked, fg="white", bg="#333333")
btn6.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn_minus = Button(row2, text="-", font="Segoe 23", relief=GROOVE, bd=0, command=btn_minus_clicked, fg="white",
                   bg="#333333")
btn_minus.pack(side=LEFT, expand=TRUE, fill=BOTH)
row3 = Frame(root)
row3.pack(expand=TRUE, fill=BOTH)
btn7 = Button(row3, text="7", font="Segoe 23", relief=GROOVE, bd=0, command=btn7_clicked, fg="white", bg="#333333")
btn7.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn8 = Button(row3, text="8", font="Segoe 23", relief=GROOVE, bd=0, command=btn8_clicked, fg="white", bg="#333333")
btn8.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn9 = Button(row3, text="9", font="Segoe 23", relief=GROOVE, bd=0, command=btn9_clicked, fg="white", bg="#333333")
btn9.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn_multiply = Button(row3, text="*", font="Segoe 23", relief=GROOVE, bd=0, command=btn_multiply_clicked, fg="white",
                      bg="#333333")
btn_multiply.pack(side=LEFT, expand=TRUE, fill=BOTH)
row4 = Frame(root)
row4.pack(expand=TRUE, fill=BOTH)
btn_clear = Button(row4, text="Clear", font="Segoe 23", relief=GROOVE, bd=0, command=btn_clear_clicked, fg="white",
                   bg="#333333")
btn_clear.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn_dot = Button(row4, text=" • ", font="Segoe 21", relief=GROOVE, bd=0, command=dot_clicked, fg="white", bg="#333333")
btn_dot.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn0 = Button(row4, text="0", font="Segoe 23", relief=GROOVE, bd=0, command=btn0_clicked, fg="white", bg="#333333")
btn0.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn_equal = Button(row4, text="=", font="Segoe 23", relief=GROOVE, bd=0, command=btn_equal_clicked, fg="white",
                   bg="#333333")
btn_equal.pack(side=LEFT, expand=TRUE, fill=BOTH)
btn_divide = Button(row4, text="/", font="Segoe 23", relief=GROOVE, bd=0, command=btn_divide_clicked, fg="white",
                    bg="#333333")
btn_divide.pack(side=LEFT, expand=TRUE, fill=BOTH)
row5 = Frame(root)
row5.pack(expand=TRUE, fill=BOTH)
sin_btn = Button(row5, text="sin", font="Segoe 18", relief=GROOVE, bd=0, command=sin_clicked, fg="white", bg="#333333")
sin_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
cos_btn = Button(row5, text="cos", font="Segoe 18", relief=GROOVE, bd=0, command=cos_clicked, fg="white", bg="#333333")
cos_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
tan_btn = Button(row5, text="tan", font="Segoe 18", relief=GROOVE, bd=0, command=tan_clicked, fg="white", bg="#333333")
tan_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)
rand_btn = Button(row5, text="rand", font="Segoe 18", relief=GROOVE, bd=0, command=rand_clicked, fg="white",
                  bg="#333333")
rand_btn.pack(side=LEFT, expand=TRUE, fill=BOTH)

# Example to show that the code is documented
help(scientificCalc)

# Starting the program infinite event loop till we terminate it
root.mainloop()
