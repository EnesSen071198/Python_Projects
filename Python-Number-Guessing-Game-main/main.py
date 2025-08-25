import random
import tkinter as tk
from tkinter import messagebox

def new_game():
    global target_number
    target_number = random.randint(1, 100)
    guess_count.set(0)
    result_label.config(text="I have picked a number between 1 and 100. Try to guess it!")  # Oyun başlangıç mesajı

def make_guess():
    try:
        guess = int(entry.get())
        guess_count.set(guess_count.get() + 1)
        if guess < target_number:
            result_label.config(text="Try a larger number.")  # Daha büyük bir sayı deneyin
        elif guess > target_number:
            result_label.config(text="Try a smaller number.")  # Daha küçük bir sayı deneyin
        else:
            messagebox.showinfo("Congratulations!", f"You found the correct answer {target_number} in {guess_count.get()} guesses!")
            new_game()
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number.")  # Geçerli bir sayı girin uyarısı

# Main Window - Ana Pencere
window = tk.Tk()
window.title("Number Guessing Game")

guess_count = tk.IntVar()

# UI Elements - Arayüz Elemanları
label = tk.Label(window, text="I have picked a number between 1 and 100. Try to guess it!")  # Başlangıç mesajı
label.pack()

entry = tk.Entry(window)
entry.pack()

guess_button = tk.Button(window, text="Make Guess", command=make_guess)
guess_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

new_game_button = tk.Button(window, text="New Game", command=new_game)
new_game_button.pack()

# Start the game - Oyunu Başlat
new_game()

window.mainloop()
