import tkinter as tk

gui = tk.Tk()
# set the background colour of GUI window 
gui.configure(background="pink")
 
# set the title of GUI window 
gui.title("Simple Calculator") 
 
# set the configuration of GUI window 
gui.geometry("270x150")


gui.mainloop()

import tkinter as tk


#Creating main window
root = tk.Tk()
root.title("Manual Calculator")

#Creating entry widget
entry = tk.Entry(root, width=35, borderwidth=15)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)