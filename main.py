import tkinter as tk
import fnmatch 
import os
from pygame import mixer


# Canvas
display = tk.Tk()
display.title("Music Player")
display.geometry("500x500")
display.config(bg = 'black')

# Where our music is
rootpath = "C:\\Users\Ashto\OneDrive\Desktop\music" 
pattern = "*.wav"

# Assets 
prev_img = tk.PhotoImage(file = "./Assets/prev_img.png")
stop_img = tk.PhotoImage(file = "./Assets/stop_img.png")
play_img = tk.PhotoImage(file = "./Assets/play_img.png")
pause_img = tk.PhotoImage(file = "./Assets/pause_img.png")
next_img = tk.PhotoImage(file = "./Assets/next_img.png")



# Music List
musicList = tk.Listbox(display, fg="cyan", bg="black", width= 100)
musicList.pack(padx = 15, pady = 15)


label = tk.Label(display, text = '', bg = 'black', fg = 'yellow')
label.pack(pady = 15)

# Layout Of Controls 
top = tk.Frame(display, bg = "black")
top.pack(padx = 10, pady = 5, anchor = 'center')

# Controls
prevButton = tk.Button(display, text="Prev", image = prev_img, bg="black", borderwidth = 0)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(display, text="Stop", image = stop_img, bg="black", borderwidth = 0)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(display, text="Stop", image = play_img, bg="black", borderwidth = 0)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(display, text="Stop", image = pause_img, bg="black", borderwidth = 0)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(display, text="Stop", image = next_img, bg="black", borderwidth = 0)
nextButton.pack(pady = 15, in_ = top, side = 'left')

# Finds all files in rootpath that match the pattern we declared. 
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        musicList.insert('end', filename) # Inserts at the end of the musicList


# Main Loop
display.mainloop()
