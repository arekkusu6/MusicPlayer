import tkinter as tk
import os
import pygame 
from pygame import mixer


# Selects and plays the song
def play():
    song = musicList.get(tk.ACTIVE)
    mixer.music.load(song)
    song_status.set(f'Playing {song}')
    mixer.music.play()

def pause():
    song_status.set("Paused")
    mixer.music.pause()

def stop():
    song_status.set("Stopped")
    mixer.music.stop()

def resume():
    song_status.set("Resuming")
    mixer.music.unpause()

# Canvas
display = tk.Tk()
display.title("Music Player")
display.geometry("500x500")
display.config(bg = 'black')

# Pygame Mixer
mixer.init()
song_status = tk.StringVar()
song_status.set("Select A Song")

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
