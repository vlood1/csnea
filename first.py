# This is the first main entrance window that the user will see upon startup of the program.

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("1000x1200")
        self.resizable(False, False) # non resizable window

        # Creating a label to display welcome message
        self.label = ttk.Label(self, text="Welcome to the Main Window!")
        self.label.place(x=200, y=50)

        # Create a button to show a message
        self.button = ttk.Button(self, text="Test Button", command=self.show_message)
        self.button.place(x=250, y=100)

    def show_message(self):
        messagebox.showinfo("Information", "You clicked the button!")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()