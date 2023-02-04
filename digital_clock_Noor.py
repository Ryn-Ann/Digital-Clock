""" 
Digital Clock 
A simple digital clock written in Python using Tkinter library

Noor Kamaruddin 5 February 2023
"""

# Import libraries
from tkinter import Label, Tk
import time

# Define the clock's title and size
clock_window = Tk()
clock_window.title("Digital Clock by Noor")
clock_window.geometry("430x175")
clock_window.resizable(0, 0)

# Define the clock's font, colour, border width and background colour
clock_font = ("Segoe UI", 72, "bold")
background = "black"
foreground = "white"
border_width = 24

# Define the label of the clock
label = Label(clock_window, font=clock_font, bg=background,
              fg=foreground, bd=border_width)
label.grid(row=0, column=1)

# Define the main function of the clock
def digital_clock():
    time_now = time.strftime("%H:%M:%S")
    label.config(text=time_now)
    label.after(200, digital_clock)

# Run to see output!
digital_clock()
clock_window.mainloop()
