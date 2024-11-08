# 4 gewinnt!

# Imports von Packages
from tkinter import *
from tkinter import font

# Fenster erstellen
main_window = Tk()
main_window.geometry("500x350")
main_window.title("4 gewinnt - Start")
# TODO: insert icon

# Fonts definieren
TITLE = font.Font(family="Arial", size=18, weight="bold")
BUTTON = font.Font(family="Arial", size=12)

# Elemente erstellen
title_main_window = Label(main_window, text="4 gewinnnt!", font=TITLE)
option_game_multiplayer = Button(main_window, text="Mehrspieler", width=12, height=2, font=BUTTON)

# Elemente platzieren
title_main_window.pack(pady=10)
option_game_multiplayer.pack()


# MAINLOOP
main_window.mainloop()