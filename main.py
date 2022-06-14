import tkinter as tk
import fnmatch 
import os
from pygame import mixer


# Canvas
display = tk.Tk()
display.title("Music Player")
display.geometry("500x500")
display.config(bg = 'black')

# Variables 
rootpath = "C:\\Users\Ashto\OneDrive\Desktop\music" 
pattern = "*.wav"

# Music List
musicList = tk.Listbox(display, fg="cyan", bg="black", width= 100)
musicList.pack(padx = 15, pady = 15)


label = tk.Label(display, text = '', bg = 'black', fg = 'yellow')
label.pack(pady = 15)

# Layout Of Controls 
top = tk.Frame(display, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

# Controls
prevButton = tk.Button(display, text="Prev")
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(display, text="Stop")
stopButton.pack(pady = 15, in_ = top, side = 'left')

# Finds all files in rootpath that match the pattern we declared. 
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        musicList.insert('end', filename) # Inserts at the end of the musicList

 # Main Loop
display.mainloop()
