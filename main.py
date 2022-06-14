import tkinter as tk
import os
from pygame import mixer


# Selects and plays the song
def play():
    song = musicList.get(tk.ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pause():
    mixer.music.pause()

def stop():
    mixer.music.stop()

def resume():
    mixer.music.unpause()

# Canvas
display = tk.Tk()
display.title("Music Player")
display.geometry("500x500")
display.config(bg = 'black')

# Pygame Mixer
mixer.init()

# Playlist
os.chdir(r'D:\Playlist')
musicList = tk.Listbox(display, selectmode=tk.SINGLE, fg="cyan", bg="black", width= 100)
musicList.pack(padx = 15, pady = 15)
songs = os.listdir()
for s in songs:
    musicList.insert(tk.END, s)


# Label 
label = tk.Label(display, text = '', bg = 'black', fg = 'yellow')
label.pack(pady = 15)

# Layout Of Controls 
top = tk.Frame(display, bg = "black")
top.pack(padx = 20, pady = 5, anchor = 'center')

# Controls
stopButton = tk.Button(display, text="Stop", bg="blue", borderwidth = 0, command = stop)
stopButton.pack(pady = 20, padx = 20, in_ = top, side = 'left')

playButton = tk.Button(display, text="Play", bg="blue", borderwidth = 0, command = play)
playButton.pack(pady = 20, padx = 20, in_ = top, side = 'left')

pauseButton = tk.Button(display, text="Pause", bg="blue", borderwidth = 0, command = pause)
pauseButton.pack(pady = 20, padx = 20, in_ = top, side = 'left')

resumeButton = tk.Button(display, text="Resume", bg="blue", borderwidth = 0, command = resume)
resumeButton.pack(pady = 20, padx = 20, in_ = top, side = 'left')

# Main Loop
display.mainloop()
