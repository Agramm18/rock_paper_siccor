
Rock-Paper-Scissors Game

A simple Python-based Rock-Paper-Scissors game where you play against the computer! This game implements the basic mechanics of Rock-Paper-Scissors, with options to play multiple rounds, track scores, and end the game whenever you choose.

Features

- Interactive Gameplay: Choose between "rock", "paper", or "scissors" to compete against a random computer choice.
- Score Tracking: Scores for both player and computer are tracked across multiple rounds.
- Input Validation: Ensures players enter valid choices and commands.
- Flexible Ending: End the game whenever you like, and view the final score for both sides.

Requirements

Python: This code is compatible with Python 3.

How to Play

1. Clone or download this repository.
2. Run the script with:
   ```bash
   python3 rock_paper_scissors.py
   ```
3. Follow the prompts to:
   - Choose between "rock", "paper", or "scissors" each round.
   - Decide whether to continue or end the game after each round.

## Game Rules

1. Choices: Each player (you and the computer) can choose one of three options: rock, paper, or scissors.
2. Winning Conditions:
   - Rock beats Scissors.
   - Scissors beat Paper.
   - Paper beats Rock.
3. Ties: If both players choose the same option, the round is a tie with no points awarded.
4. Game End: At the end of each round, you may choose to either continue or end the game.

## Code Structure

- Game` Class: The main class containing the game logic.
  - Attributes:
    - player_points` and computer_points: Track the current round’s points.
    - player_final_scores` and `computer_final_scores`: Store final scores across games.
  - Methods:
    - `play_game()`: Runs the main game loop, handles input, and checks winning conditions.
