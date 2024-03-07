
import tkinter as tk

#Creating main window
root = tk.Tk()
root.title("Manual Calculator")
root.configure(background="light pink")
root.config(cursor="hand2", relief="groove", bd=15)
custom_font = ("Georgia", 16)

#Creating entry widget
display = tk.Entry(root,font=custom_font, width=45, borderwidth=15)
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

#Defining the functions
def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def clear():
    display.delete(0, tk.END)

def equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

#Defining buttons
buttons = [
    ("1", lambda: button_click("1")),
    ("2", lambda: button_click("2")), 
    ("3", lambda: button_click("3")), 
    ("4", lambda: button_click("4")),
    ("5", lambda: button_click("5")), 
    ("6", lambda: button_click("6")), 
    ("7", lambda: button_click("7")), 
    ("8", lambda: button_click("8")),
    ("9", lambda: button_click("9")), 
    ("0", lambda: button_click("0")),
    ("00", lambda: button_click("00")),
    ("+", lambda: button_click("+")),
    ("-", lambda: button_click("-")),
    ("*", lambda: button_click("*")),
    ("/", lambda: button_click("/")),
    (".", lambda: button_click(".")),
    ("C", clear),
    ("=", equal)
]

#Adding buttons to the grid
row_num = 1
col_num = 0
for (text, command) in buttons:
    if text == "=":
        tk.Button(root, text=text, bg="light green", font=custom_font, padx=30, pady=20, command=command).grid(row=row_num, column=col_num, columnspan=3, sticky="nsew")
       
        col_num += 2  
    else:
        tk.Button(root, text=text, bg="light green", font=custom_font, padx=30, pady=20, command=command).grid(row=row_num, column=col_num, sticky="nsew")
        
        col_num += 1

    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()