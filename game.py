from tkinter import *

# gt = gametype 1 [against computer] oder 2 [Mehrspieler]
class GameWindow():
    def __init__(self, gt):
        self.game_window = Tk()
        self.game_window.geometry("900x650")
        # Spielmodus -> entsprechender Titel
        if gt == 1:
            self.game_window.title("Gegen Computer - Spiel")
        else:
            self.game_window.title("Mehrspieler - Spiel")
        
        # Board zeichnen
        self.drawBoard()

    def drawBoard(self):
        self.board = []
        for _ in range(7):  # Spalten
            spalte = []
            for _ in range(6):
                spalte.append(0)
            self.board.append(spalte)  # Füge die Spalte zur Liste der Zeilen hinzu

    

    def __repr__(self) -> str:
        return f"{self.board}"

if __name__ == "__main__":
    game = GameWindow(2)  # Erstelle eine Instanz von GameWindow
    print(game)  # Gibt die Darstellung des Boards aus
    game.game_window.mainloop()  # Starte die Tkinter-Hauptschleife