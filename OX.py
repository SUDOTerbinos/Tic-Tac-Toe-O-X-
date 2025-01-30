import tkinter as tk
from tkinter import messagebox

def check_winner():
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return row[0]["text"]
    
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            return board[0][col]["text"]
    
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return board[0][0]["text"]
    
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return board[0][2]["text"]
    
    return None

def on_click(row, col):
    global turn
    if board[row][col]["text"] == "" and not winner:
        board[row][col]["text"] = "X" if turn else "O"
        turn = not turn
        winner_check()

def winner_check():
    global winner
    winner = check_winner()
    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        reset_board()
    elif all(board[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()

def reset_board():
    global turn, winner
    turn = True
    winner = None
    for i in range(3):
        for j in range(3):
            board[i][j]["text"] = ""

root = tk.Tk()
root.title("Tic-Tac-Toe")

turn = True  
winner = None

board = [[tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda r=i, c=j: on_click(r, c)) for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        board[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3)

root.mainloop()
