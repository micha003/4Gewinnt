# Dokumentation "4 Gewinnt"

*von Michael V. und Paul V.*

---

Das Projekt besteht hauptsächlich aus den beiden Dateien `main.py` und `game.py`. Das Skript `main.py` enthält das Hauptmenü und die Zusammenführung der Spiellogik, während `game.py` die Spiellogik ansich enthält.

## `main.py`

Zunächst werden alle benötigten Module importiert in Zeile 4 bis 6:

```python
from tkinter import *
from tkinter import font
from game import Game
```

Dann wird das Hauptmenüfenster erstellt und auch ein entsprechender Titel für das Fenster gesetzt. In Zeile 15 werden die Schriftarten (*fonts*) definiert, um einen einheitlichen Look zu erhalten:

```python
# Fonts definieren
TITLE = font.Font(family="Arial", size=18, weight="bold")
BUTTON = font.Font(family="Arial", size=12)
```

Im Anschluss wird das Herzstück des Hauptfensters abgefasst, nämlich der Titel und die beiden Buttons, die zu den beiden verfügbaren Spielmodi führen.

```python
title_main_window = Label(main_window, text="4 gewinnnt!", font=TITLE)
option_game_multiplayer = Button(
    main_window,
    text="2 Spieler",
    width=12,
    height=2,
    font=BUTTON,
    command=lambda: Game(2),
)

option_game_singleplayer = Button(
    main_window,
    text="Einzelspieler",
    width=12,
    height=2,
    font=BUTTON,
    command=lambda: Game(1),
)
```

Die beiden Buttons sind auch mit einem *Command* belegt, welcher über eine anonyme (Lambda-) Funktion eine Instanz der Klasse `Game` erstellt, wobei der Spielmodus als Parameter übergeben wird.

Zuletzt werden die drei Elemente mit Hilfe der `pack`-Methode auf dem Hauptfenster angeordnet und das Fenster selbst mit `mainloop` gestartet:

```python
# Elemente platzieren
title_main_window.pack(pady=10)
option_game_multiplayer.pack()
option_game_singleplayer.pack()


# MAINLOOP
main_window.mainloop()
```

Bei der Ausführung dieses Codes wird ein Fenster mit einem Titel und zwei Buttons angezeigt. Hier auch interessant Parameter bei der Platzierung des Fenstertitels `pady`, welcher lediglich den Abstand zwischen dem Text bzw. Inhalt des Labels und dem Rand des Fensters erhöht. Die beiden Buttons werden direkt untereinander angeordnet.

## `game.py`
