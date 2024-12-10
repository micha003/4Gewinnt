from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
import random


# gt = gametype 1 [against computer] oder 2 [Mehrspieler]
class Game:
    def __init__(self, gt):
        self.game_window = Tk()
        self.game_window.geometry("850x800")
        self.current_player = 1  # Spieler 1 beginnt
        self.game_over = False
        self.gt = gt

        # Farbwahl
        self.color_window = Tk()
        self.color_window.geometry("500x200")
        # self.color_window.overrideredirect(True)
        self.color_window_label = Label(
            self.color_window, text="Bitte wähle die Farben!"
        )

        self.colors = ["red", "yellow", "blue", "green"]

        self.color_window_label_1 = Label(self.color_window, text="Spieler 1")
        self.color_window_label_2 = Label(self.color_window, text="Spieler 2")

        self.drop1 = Combobox(self.color_window, values=self.colors)
        self.drop2 = Combobox(self.color_window, values=self.colors)

        self.OK_button = Button(
            self.color_window,
            text="OK",
            command=lambda: self.check_colors(
                color1=self.drop1.get(), color2=self.drop2.get()
            ),
        )

        self.color_window_label.grid(column=1, row=0)
        self.color_window_label_1.grid(column=0, row=1)
        self.color_window_label_2.grid(column=2, row=1)
        self.drop1.grid(column=0, row=2)
        self.drop2.grid(column=2, row=2)
        self.OK_button.grid(column=1, row=3)

        if self.gt == 1:
            self.game_window.title("Gegen Computer - Spiel")
        else:
            self.game_window.title("Mehrspieler - Spiel")

        self.drawBoard()

    def check_colors(self, color1, color2):
        if color1 == color2:
            return
        else:
            self.color_player1 = color1
            self.color_player2 = color2
            self.color_window.destroy()

    def drawBoard(self):
        self.board = [[0 for _ in range(6)] for _ in range(7)]  # 7 Spalten, 6 Reihen

        for col in range(7):
            col_button = Button(
                self.game_window,
                text=col + 1,
                width=8,
                height=5,
                command=lambda c=col: self.drop_piece(c),
            )
            col_button.grid(row=0, column=col)

        self.current_player_label = Label(
            self.game_window, text=f"Spieler {self.current_player} ist am Zug"
        )
        self.current_player_label.grid(row=0, column=7, columnspan=7)

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

    def drop_piece(self, col):
        # wenn zeile voll
        if self.board[col][0] != 0:
            showinfo("Fehler", "Diese Spalte ist bereits voll!")
            return

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

        if self.gt == 1 and self.current_player == 2:
            column = random.choice([col for col in range(7) if self.board[col][0] == 0])
            self.drop_piece(column)

        if all(self.board[col][0] != 0 for col in range(7)):
            print("Unentschieden!")
            showinfo("Game Over", "Das Spiel ist unentschieden.")
            self.game_window.destroy()

    def draw_piece(self, col, row):
        x1 = col * self.cell_width
        y1 = row * self.cell_height + 50
        x2 = x1 + self.cell_width
        y2 = y1 + self.cell_height
        color = self.color_player1 if self.current_player == 1 else self.color_player2
        self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def check_winner(self, col, row):
        # Überprüfen auf Gewinnbedingungen (horizontal, vertikal, diagonal)
        return (
            self.check_direction(col, row, 1, 0)  # horizontal
            or self.check_direction(col, row, 0, 1)  # vertikal
            or self.check_direction(col, row, 1, 1)  # diagonal
            or self.check_direction(col, row, 1, -1)  # diagonal
        )

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

    def __repr__(self) -> str:
        return f"{self.board}"


if __name__ == "__main__":
    game = Game(1)  # Erstelle eine Instanz von GameWindow
    print(game)  # Gibt die Darstellung des Boards aus
    game.game_window.mainloop()  # Starte die Tkinter-Hauptschleife
