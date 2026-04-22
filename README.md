📌 Overview
This project is a Python implementation of the game Rock–Paper–Scissors–Lizard–Spock, a popular extension of the classic Rock–Paper–Scissors game.
The program allows a player to choose an option and then randomly generates a computer choice. The winner is determined using modular arithmetic, following the official game rules.

🧠 Game Rules
Each option defeats two others and loses to two:

Rock crushes Scissors, crushes Lizard
Paper covers Rock, disproves Spock
Scissors cuts Paper, decapitates Lizard
Lizard eats Paper, poisons Spock
Spock smashes Scissors, vaporizes Rock

A tie occurs when both choices are the same.

⚙️ How the Program Works
The project includes the following key functions:


name_to_nums(name)
Converts a move name (e.g., "Rock") into a number.


nums_to_names(nums)
Converts a number back into a move name.


rpsls(player_choice)

Takes the player’s choice as input
Randomly generates a computer choice
Uses (player_number - computer_number) % 5 to determine the winner
Prints the result (Player wins, Computer wins, or Tie)




▶️ Example Output
Player chooses Rock
Computer chooses Spock
Computer Wins!
🛠️ Technologies Used

Python 3
random module (for computer choice)


▶️ How to Run

Make sure Python 3 is installed
Save the script as rpsls.py
python rps
python rpsShow more lines

The game will automatically run with predefined player choices:

Rock
Spock
Paper
Lizard
Scissors




📚 Educational Purpose
This project was created for learning purposes and demonstrates:

Function design
Conditional logic
Random number generation
Modular arithmetic
Mapping between strings and numbers


✅ Notes

Input choices are case‑sensitive
The game logic follows the standard RPSLS algorithm
Designed as a simple console-based implementation
