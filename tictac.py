import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []

    
        for idx in range(9):
            btn = tk.Button(
                root,
                text="",
                font=("Helvetica", 32),
                width=3,
                height=1,
                command=lambda i=idx: self.on_click(i)
            )
            btn.grid(row=idx//3, column=idx%3)
            self.buttons.append(btn)


        restart = tk.Button(
            root,
            text="Reiniciar",
            font=("Helvetica", 14),
            command=self.reset_game
        )
        restart.grid(row=3, column=0, columnspan=3, sticky="we")

    def on_click(self, index):
        if self.board[index] or self.check_winner():
            return


        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)


        if self.check_winner():
            messagebox.showinfo("Parabéns!", f"Jogador {self.current_player} venceu!")
        elif all(self.board):
            messagebox.showinfo("Empate", "O jogo terminou em empate!")
        else:

            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        combos = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a]:
                for i in (a, b, c):
                    self.buttons[i].config(bg="lightgreen")
                return True
        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [None] * 9
        for btn in self.buttons:
            btn.config(text="", bg="SystemButtonFace")

if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeGUI(root)
    root.mainloop()
