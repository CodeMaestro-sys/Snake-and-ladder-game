# Snake-and-ladder-game
Python implementation of the snake and ladder game with a computer opponent

# 🎲 Snake and Ladder Game (Python)

This is a simple command-line based **Snake and Ladder** game in Python, where a human player competes against the computer. The game follows standard snake and ladder rules, with the goal of reaching position 100.

---

## 🧩 Game Features

- 🧑‍💻 **Two players**: You (Player 1) vs. the Computer (Player 2)
- 🎲 **Random dice roll** using random.randint(1, 6)
- 🐍 **Snakes**: Slide down when you land on a snake's head
- 🪜 **Ladders**: Climb up when you land at the base of a ladder
- 🚫 **Rolls over 100** are skipped
- 🏁 Game ends when a player reaches position 100

---

## 🪜 Snakes & Ladders

- **Ladders:**  
  1 → 38, 4 → 14, 8 → 30, 21 → 42, 28 → 76, 50 → 67, 71 → 92, 80 → 99

- **Snakes:**  
  32 → 10, 36 → 6, 48 → 26, 62 → 18, 88 → 24, 95 → 56, 97 → 78

---

## ▶️ How to Run

### Prerequisites
- Python 3.x installed on your system

### Running the Game

1. Download the Python file:
snake_ladder_game.py

markdown
Copy
Edit

2. Open a terminal or command prompt in the file's directory.

3. Run the game:
bash
python snake_ladder_game.py
## Example output
Enter your name=Alex
Player1 is  Alex
Player2 is Computer
Turn of Player1
Your number is 6
Your new position is 6
----------+------+-------+----------
Turn of player2
Your number is 1
Your new position is 1
After climbing the ladder your new position is 38
Final position of player1 is= 6
Final position of player2 is= 38
Do you want to play again(Y/N)?
