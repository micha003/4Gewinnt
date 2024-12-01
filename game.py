from tkinter import *
from tkinter.messagebox import showinfo
import random


# gt = gametype 1 [against computer] oder 2 [Mehrspieler]
class Game:
    def __init__(self, gt):
        self.game_window = Tk()
        self.game_window.geometry("850x800")
        self.current_player = 1  # Spieler 1 beginnt
        self.game_over = False
        self.gt = gt

        if self.gt == 1:
            self.game_window.title("Gegen Computer - Spiel")
        else:
            self.game_window.title("Mehrspieler - Spiel")

        self.drawBoard()

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
        color = "red" if self.current_player == 1 else "yellow"
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
    game = Game(2)  # Erstelle eine Instanz von GameWindow
    print(game)  # Gibt die Darstellung des Boards aus
    game.game_window.mainloop()  # Starte die Tkinter-Hauptschleife
