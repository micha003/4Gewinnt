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

Die Spiellogik befindet sich hier in dieser Datei, genauergesagt in der Kl
Klasse `Game`.  Jedes Mal, wenn im Hauptmenü einer der beiden Buttons gedrückt
wird, die ein Spiel starten sollen, wird eine Instanz der Klasse erstellt.

Zunächst werden die notwendigen Imports durchgeführt, um die erforderlichen Module
bereitzustellen (Zeilen 1-4):

```python
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
import random
```

- `tkinter`: Modul für die Erstellung von GUIs
- `tkinter.messagebox`: Untermnodul von `tkinter` für die Erstellung von Pop-Up-Fenstern
- `tkinter.ttk`: Untermmodul von `tkinter` für die Erstellung von Drop-Down-Menüselbs
- `random`: Modul, womit man zufällige Werte generieren kann

---

Ab Zeile 8 wird die Klasse `Game` definiert:

```python
class Game:
    def __init__(self, gt):
        self.game_window = Tk()
        self.game_window.geometry("850x800")
        self.current_player = 1  # Spieler 1 beginnt
        self.game_over = False
        self.gt = gt
```

Die `__init__` -Methode, auch als Konstruktur bekannt, ist eine Methode, die ein Mal bei der Instanzierung
der Klasse aufgerufen wird. Sie kann auch Parameter nehmen, wie hier `gt`. Diese Parameter
werden einfach bei der Instanzierung der Klasse übergeben in den Klammern (`Game(1)`).

|Variable|Datentyp|Verwendung|
|:---:|:---:|:---:|
|`self.game_window`|Tk (Objekt)|Root-Objekt für das Spielfenster|
|`self.current_player`|Integer|Angabe aktueller Spieler|
|`self.game_over`|Boolean|Angabe, ob das Spiel beendet ist|
|`self.gt`|Integer|Parameter, der übergeben bei der Instanzierung|

Im Anschluss haben wir das zusätzliche Feature eingebaut, dass man die Farben für die Spieler festlegen kann.
Dabei kommt die `Combox`-Klasse zum Einsatz. Hiermit wird gleich ein Drop-Down-Menü erstellt,
in dem man die Farben auswählen kann.

```python
# Farbwahl
        self.color_window = Tk()
        self.color_window.geometry("500x200")
        self.color_window_label = Label(
            self.color_window, text="Bitte wähle die Farben!"
        )
```

Hier wird das Fenster für die Farbwahl erstellt. Im Anschluss werden die Fensterdimensionen festegelegt,
sowie ein Label erstellt, was als Überschrift für das Fenster fungiert.

```python
self.colors = ["red", "yellow", "blue", "green"]
```

Das ist die Liste, die die verfügbaren Farben enthält. Diese Liste kann beliebig erweitert werden.

```python
        self.color_window_label_1 = Label(self.color_window, text="Spieler 1")
        self.color_window_label_2 = Label(self.color_window, text="Spieler 2")

        self.drop1 = Combobox(self.color_window, values=self.colors)
        self.drop2 = Combobox(self.color_window, values=self.colors)
```

Hier werden die Labels für die Drop-Down-Menüs erstellt, sowie die Drop-Down-Menüs selbst für die Farbauswahl.
Als Paramater für das Drop-Down-Menü übergebe ich in `values` die Liste `colors` der verfügbaren Farben.

```python
        self.OK_button = Button(
            self.color_window,
            text="OK",
            command=lambda: self.check_colors(
                color1=self.drop1.get(), color2=self.drop2.get()
            ),
        )
```

Hier wird der *OK*-Button erstellt, der das Fenster schließt, wenn Farben ausgewählt wurden. Wenn keine oder gleiche Farben
ausgewählt werden, dann schließt er das Fenster nicht. Wie die evaluierende Methode `check_colors` funktioniert, wird in Kürze erläutert.

*An dieser Stelle könnte man implementieren, dass man das Fenster nicht mit den normalen Schaltflächen am Bildschirmrand schließen kann.*

```python
self.color_window_label.grid(column=1, row=0)
self.color_window_label_1.grid(column=0, row=1)
self.color_window_label_2.grid(column=2, row=1)
self.drop1.grid(column=0, row=2)
self.drop2.grid(column=2, row=2)
self.OK_button.grid(column=1, row=3)
```

Zuletzt werden nochmal die ganzen Elemente mithilfe der `grid`-Methode  geordnet im Fenster platziert.
In Relation zu den Fensterdimensionen werden die Elemente wie in einer Tabelle angeordnet mit Zeilen und Spalten.

Die `__init__`-Methode endet mit der Evaluierung der `gt`-Variable und dem Aufruf der Methode `drawBoard`:

```python
if self.gt == 1:
    self.game_window.title("Gegen Computer - Spiel")
else:
    self.game_window.title("Mehrspieler - Spiel")

self.drawBoard()
```

Ersteres bestimmt den Titel des Spielfensters. Die `drawBoard`-Methode` wird verwendet, um das Spielfeld zu
zeichnen. *Mehr dazu in Kürze.*

---

```python
def check_colors(self, color1, color2):
        if color1 == color2:
            return
        else:
            self.color_player1 = color1
            self.color_player2 = color2
            self.color_window.destroy()
```

Die Methode `check_colors` wird aufgerufen, wenn der *OK*-Button gedrückt wird. Sie überprüft, ob die beiden ausgewählten
Farben gleich sind. Wenn ja, dann wird nichts zurückgegeben (Es passiert nichts :o). Ansonsten werden die beiden
lokalen Variablen in Instanzvariablen gespeichert. Das Fenster wird geschlossen durch `self.color_window.destroy()`.

Mit `drawBoard`-Methode wird das Feld gezeichnet. Zunächst wird ein zweidimensionales Array
generiert:

```python
self.board = [[0 for _ in range(6)] for _ in range(7)]
```

Also es wird für jede Zeile ein Array mit 6 Elementen erstellt. Das Ganze sieben Mal, weil
es gibt 7 Spalten.

Für jede Spalte wird ein Button erstellt, den man klicken kann, um seinen Spielstein zu platzieren:

```python
for col in range(7):
    col_button = Button(
        self.game_window,
        text=col + 1,
        width=8,
        height=5,
        command=lambda c=col: self.drop_piece(c),
    )
    col_button.grid(row=0, column=col)
```

Jeder dieser Buttons wird aucht mit der `drop_piece`-Methode belegt, damit dann auf der Canvas (Spielfeld)
ein Spielstein in entsprechender Farbe plaziert wird.

Ein weiteres zusätzliches Feature, was wir eingebaut haben, ist die Anzeige des aktuellen Spielers:

```python
self.current_player_label = Label(
    self.game_window, text=f"Spieler {self.current_player} ist am Zug"
    )
self.current_player_label.grid(row=0, column=7, columnspan=7)
```

Für die grafische Umsetzung des Feldes wird eine Canvas (Built-in-Feature von Tkinter) erstellt:

```python
self.canvas = Canvas(
    self.game_window,
    width=700,
    height=800,
)
self.canvas.grid(row=1, column=0, columnspan=7)

self.cell_width = 100
self.cell_height = 100

for col in range(7):
    for row in range(6):
        x1 = col * self.cell_width
        y1 = row * self.cell_height + 50
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height
        self.canvas.create_rectangle(
            x1, y1, x2, y2, outline="black", fill="white"
        )
```

In der letzten for-Loop werden die einzelnen, später befüllten, Kästchen generiert.

---

Die entscheidende Methode, die die Spiellogik steuert im Endeffekt, ist die `drop_piece`-Methode:

```python
def drop_piece(self, col):
    # wenn zeile voll
    if self.board[col][0] != 0:
        showinfo("Fehler", "Diese Spalte ist bereits voll!")
        return
```

Dieser erste Ausschnitt der Methode prüft, ob die als Parameter mitgegebene Spalte bereits voll ist.
Dort kann logischerweise kein Stein mehr platziert werden.

```python
# Finde die nächste freie Zeile in der gewählten Spalte
for row in range(5, -1, -1):
    if self.board[col][row] == 0:
        self.board[col][row] = self.current_player
        self.draw_piece(col, row)
        if self.check_winner(col, row):
            print(f"Spieler {self.current_player} hat gewonnen!")
            showinfo(
                "Game Over",
                f"Das Spiel ist vorbei! Spieler {self.current_player} hat gewonnen.",
            )
            self.game_window.destroy()
            return
        self.current_player = (
            2 if self.current_player == 1 else 1
        )  # Wechseln des Spielers
        self.current_player_label.config(
            text=f"Spieler {self.current_player} ist am Zug"
        )
        break
```

Die "große" for-Schleife beginnt bei dem Wert 5 (Zeile 6) und geht immer einen Schritt nach unten (-1),
bis sie eine freie Zeile in der gewählten Spalte gefunden hat. Im Anschluss wird die Zahl des aktuellen Spielers
in das zweidimensionale Array `self.board` eingetragen und die Methode `draw_piece` wird aufgerufen, welche dann den Spielstein
malt.

Die `draw_piece`-Methode ist auch kein Hexenwerk; es zeichnet einfach einen Kreis in das jeweilige Kästchen mit
den bereits festegelegten Farben.

```python
def draw_piece(self, col, row):
        x1 = col * self.cell_width
        y1 = row * self.cell_height + 50
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height
        color = self.color_player1 if self.current_player == 1 else self.color_player2
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)
```

Es gibt ja keine Spielschleife / Hauptschleife im klassischen Sinne. Wir haben es so gelöst, dass jedes Mal,
wenn ein Stein gesetzt wurde, auch direkt geprüft wird, ob ein Spieler gewonnen hat. Dazu haben wir die Methode `check_winner` erstellt:

```python
def check_winner(self, col, row):
    # Überprüfen auf Gewinnbedingungen (horizontal, vertikal, diagonal)
    return (
        self.check_direction(col, row, 1, 0)  # horizontal
        or self.check_direction(col, row, 0, 1)  # vertikal
        or self.check_direction(col, row, 1, 1)  # diagonal
        or self.check_direction(col, row, 1, -1)  # diagonal
    )
```

Die hier mehrfach aufgerufene Methode `check_direction` prüft, ob es in einer bestimmten Richtung mehrere Spielsteine des
gleichen Spielers gibt:

```python
def check_direction(self, col, row, delta_col, delta_row):
    count = 0  # Zähle den aktuellen Stein

    # Überprüfen in positiver Richtung
    for i in range(-3, 4, 1):
        new_col = col + i * delta_col
        new_row = row + i * delta_row
        if 0 <= new_col < 7 and 0 <= new_row < 6:
            if self.board[new_col][new_row] == self.current_player:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
        return False
```

Diese Methode ist sehr interessant und zwar dahingehend, dass sie neben den Paramtern `col` und `row` auch noch zwei weitere
Parameter nimmt: `delta_col` und `delta_row`. Diese beiden Parameter bestimmen die Richtung, in welche Richtung
die Methode prüfen soll. Die Bezeichnung *delta* wurde hier verwendet aufgrund des Kontextes in der Mathematik und Physik,
wo der griechische Buchstabe Delta (Δ) oft verwendet wird, um eine Änderung oder Differenz darzustellen.

---

Zurück zur Methode `drop_piece`:

```python
# Finde die nächste freie Zeile in der gewählten Spalte
for row in range(5, -1, -1):
    if self.board[col][row] == 0:
        self.board[col][row] = self.current_player
        self.draw_piece(col, row)
        if self.check_winner(col, row):
            print(f"Spieler {self.current_player} hat gewonnen!")
            showinfo(
                "Game Over",
                f"Das Spiel ist vorbei! Spieler {self.current_player} hat gewonnen.",
            )
            self.game_window.destroy()
            return
        self.current_player = (
            2 if self.current_player == 1 else 1
        )  # Wechseln des Spielers
        self.current_player_label.config(
            text=f"Spieler {self.current_player} ist am Zug"
        )
        break
```

Falls die Methode `check_winner` einen wahren Wert zurückgibt, dann wird ein Popup-Fenster erstellt,
wo der Sieger bekannt gegeben wird. Das Spiel wird dann beendet und das Fenster wird geschlossen. Insofern
noch keiner der beiden Spieler gewonnen hat, dann wird der aktuelle Spieler getauscht und diese Änderung
im Label auf dem Bildschirm angezeigt.

Wie man aber vielleicht schon ahnen konnte bei der Variable `self.gt`, müsste es ja mehrere Spielmodi geben.
Und ja, es gibt die Möglichkeit, nicht gegen einen zweiten Spieler zu spielen, sondern auch gegen den Computer!

```python
if self.gt == 1 and self.current_player == 2:
    column = random.choice([col for col in range(7) if self.board[col][0] == 0])
    self.drop_piece(column)
```

Da der Schwerpunkt nicht auf der Entwicklung einer KI für das Spiel lag, haben wir einfach festgelegt,
dass der Computer immer auf ein zufälliges Feld seine Spielsteine platziert.

Zuletzt wird jedoch noch auf ein Unentschieden geprüft. Wenn alle Felder auf dem Spielbrett besetzt sind bzw.
es wird nur die oberste Zeile geprüft, ob da alle Felder besetzt sind, dann ist das Spiel unentschieden.

```python
if all(self.board[col][0] != 0 for col in range(7)):
        print("Unentschieden!")
        showinfo("Game Over", "Das Spiel ist unentschieden.")
        self.game_window.destroy()
```

Am Rande kann man noch die `__repr__`-Methode erwähnen, die lediglich dazu dient, einen String zurückzugeben,
der dann in der Kommandozeile ausgegeben wird, wenn man die Variable der Instanz printen möchte. Sonst 
würde da nur eine Objektbezeichnung kommen mit der Speicherstelle im Arbeitsspeicher.

```python
def __repr__(self) -> str:
    return f"{self.board}"
```

Hier wird einfach das mehrdimensionale Array ausgegeben, was die Spielbrett darstellt.

## Spielanleitung und Hinweise

Wenn man das Spiel ganz normal spielen möchte, dann am besten sicherstellen, dass man Python 3 installiert hat.
Des Weiteren muss man die Datei `main.py` ausführen.

Sobald man dann einen Spielmodi ausgewählt hat, kann es passieren, dass das Farbauswahlfenster
dem Spielfenster ist. **Nicht** minimieren, sondern einfach, das Spielfenster beseite ziehen und die Eingaben tätigen.

Im Spiel einfach immer den Button über der Spalte anklicken, wo man seinen Spielstein platzieren möchte.

*Das Programm hat keine bekannten Bugs (10.12.2024).*

## Anteile der Gruppenmitglieder

Michael - Grundspiel
Paul - alle zusätzlichen Features (Farbauswahl, Anzeige akt. Spieler, Spiel gegen Computer)

> **Wir wünschen viel Spaß beim Spielen!**