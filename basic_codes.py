import tkinter as tk

root = tk.Tk()

# Function to be called when the button is clicked
def button_click():
    print("Button clicked")

# Create a button with a specific color
button1 = tk.Button(root, text="Button 1", bg="blue", fg="white", command=button_click)
button1.pack()

# Another button with different colors
button2 = tk.Button(root, text="Button 2", bg="green", fg="black", command=button_click)
button2.pack()

root.mainloop()
