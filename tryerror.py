import tkinter as tk

#creating the GUI window
root=tk.Tk()
root.title("Manual calculator")
custom_font = ("Helvetica", 16)

#creating the entry widget
entry = tk.Entry(root, width=35, borderwidth=15)
entry.grid(row=0, column=0, columnspan=10, padx=20, pady=20)

#defining the functions
def button_click(number):
    current=entry.get()
    entry.delete(0,tk.END)
    entry.insert(tk.END,current+str(number))

def clear():
    entry.delete(0,tk.END)

def equal():
    try:
        result=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END,result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END,"ERROR")

#defining the buttons
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

#adding buttons to the grid
row_num=1
col_num=0
for (text,command) in buttons:
    if text == "=":
       tk.Button(root, text=text, background="light green", font=custom_font, padx=20, pady=20, command=command).grid(row=row_num, column=col_num, columnspan=2, sticky="nsew")
      
       col_num+=2
    else:
       tk.Button(root, text=text, background="light green", font=custom_font, padx=20, pady=20, command=command).grid(row=row_num, column=col_num, sticky="nsew")
       col_num+=1

    if col_num>=3:
        col_num=0
        row_num+=1

root.mainloop()




