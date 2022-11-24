import webbrowser
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

# global variable
clicked = True
count = 0
winner = False
button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button1))
button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button2))
button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button3))

button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button4))
button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button5))
button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button6))

button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button7))
button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button8))
button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                 command=lambda: button_click(button9))


def explore_more_projects():
    url = "https://github.com/RajParsaniya"
    webbrowser.open_new_tab(url)
    root.destroy()


def disable_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)

    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)

    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)


def someone_won():
    global winner
    winner = False

    # Check for X
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="#008000")
        button2.config(bg="#008000")
        button3.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg="#008000")
        button5.config(bg="#008000")
        button6.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="#008000")
        button8.config(bg="#008000")
        button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="#008000")
        button4.config(bg="#008000")
        button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="#008000")
        button5.config(bg="#008000")
        button8.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="#008000")
        button6.config(bg="#008000")
        button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="#008000")
        button5.config(bg="#008000")
        button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="#008000")
        button5.config(bg="#008000")
        button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n X Win...")
        disable_buttons()

    # Check for O
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="#008000")
        button2.config(bg="#008000")
        button3.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg="#008000")
        button5.config(bg="#008000")
        button6.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="#008000")
        button8.config(bg="#008000")
        button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="#008000")
        button4.config(bg="#008000")
        button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="#008000")
        button5.config(bg="#008000")
        button8.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg="#008000")
        button6.config(bg="#008000")
        button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="#008000")
        button5.config(bg="#008000")
        button9.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="#008000")
        button5.config(bg="#008000")
        button7.config(bg="#008000")
        winner = True
        messagebox.showinfo("Tic Tac Toe", " Congratulations !!! \n O Win...")
        disable_buttons()

    if count == 9 and winner is False:
        messagebox.showinfo("Tic Tac Toe", " Ohh It's A Tie !!! \n No One Wins...")
        disable_buttons()


def button_click(b):
    global clicked, count

    # label.config(text="X")
    if b["text"] == " " and clicked is True:
        b["text"] = "X"
        clicked = False
        count += 1
        someone_won()

    elif b["text"] == " " and clicked is False:
        b["text"] = "O"
        clicked = True
        count += 1
        someone_won()

    else:
        messagebox.showerror("Tic Tac Toe", " That box has already been selected \n Please pick another one...")


def reset():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicked, count

    clicked = True
    count = 0

    # Button
    button1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button3))

    button4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button6))

    button7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="#d3d3d3",
                     command=lambda: button_click(button9))

    # Grid This 9 Buttons
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)


# Create Menu
MyCustomMenu = Menu(root)
root.config(menu=MyCustomMenu)

# Create options menu
OptionsMenu = Menu(MyCustomMenu, tearoff=False)
MyCustomMenu.add_cascade(label="Options", menu=OptionsMenu)
OptionsMenu.add_command(label="Reset Game", command=reset)
OptionsMenu.add_command(label="Explore more projects", command=explore_more_projects)

reset()
root.mainloop()
