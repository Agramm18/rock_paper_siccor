# README for Rock-Paper-Scissors Game

## Overview
Welcome to the **Rock-Paper-Scissors Game** implemented in Python! This interactive, command-line game provides a fun and engaging way to enjoy the classic game against a computer opponent. Designed with simplicity and user experience in mind, the game offers a practical example of Python programming, including coding structure, error handling, and user interaction techniques.

Whether you’re a prospective employer or a casual player, this project reflects a strong commitment to clean and maintainable code, user-friendly design, and practical application of game logic.

## Table of Contents
1. [Features](#features)
2. [Game Logic](#game-logic)
3. [Code Structure](#code-structure)
4. [Error Handling](#error-handling)
5. [How to Play](#how-to-play)
6. [Conclusion](#conclusion)

## Features
This Rock-Paper-Scissors game includes the following features:
- **User vs. Computer Gameplay**: A player competes against the computer in multiple rounds of rock-paper-scissors.
- **Score Tracking**: Both player and computer scores are recorded, along with tie counts, across rounds.
- **Dynamic Rounds**: Players can choose to continue or end the game after each round.
- **Clear Feedback**: The game provides real-time feedback on choices, scores, and round outcomes.

## Game Logic
The game follows classic rock-paper-scissors rules:
- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.
- A tie occurs if both players make the same choice.

Each round proceeds as follows:
1. The player selects `rock`, `paper`, or `scissor`.
2. The computer randomly selects one of the options.
3. The game announces the round winner based on the choices.
4. The player can decide to continue playing or end the game to view the final results.

### Winning Conditions
Once the game ends, the player’s and computer’s points are compared:
- **Player Wins** if they have more points than the computer.
- **Computer Wins** if the computer has more points.
- **Tie Count** is displayed if there were any ties.

## Code Structure
The game code is encapsulated in a `Game` class, designed to be modular, extensible, and easy to maintain. Key components include:

- **Attributes**:
  - `computer_final_scores` and `player_final_scores`: Lists to track scores across game sessions.
  - `player_points` and `computer_points`: Counters for tracking scores within a session.
  - `round`: Tracks the current round number.
  - `ties`: Tracks the number of tie rounds.

- **Methods**:
  - `__init__`: Initializes game attributes.
  - `play_game`: Main game loop and logic, handling player choices, round outcomes, and score calculations.

This class-based structure ensures code clarity and reusability, demonstrating clean organization and readiness for future extensions.

## Error Handling
The game features robust error handling for a smooth player experience:
- **Invalid Input for Choices**: If the player inputs anything other than `rock`, `paper`, or `scissor`, a `ValueError` is raised with clear instructions.
- **Game Continuation Input**: After each round, players must type 'e' to end or 'c' to continue. Invalid inputs prompt a correction.
- **User-Friendly Messages**: The game guides players through any input errors, ensuring accessibility for all.

This error handling highlights the commitment to user-focused design, ensuring reliability and guiding players with friendly messages.

## How to Play
1. **Run the Script**: Ensure Python 3.x is installed and execute the script in a terminal.
2. **Choose Your Option**: When prompted, type `rock`, `paper`, or `scissor`.
3. **View Results**: The game will display player and computer choices and announce the round winner.
4. **Continue or End**: Type 'c' to play another round or 'e' to end and see the final score.
5. **Final Scores and Winner**: Once the game ends, final scores, including ties, are displayed.

### Example Output
```plaintext
Welcome to round one! You can choose between ('rock', 'paper', 'scissor')
Please choose between these options to continue the game: rock
The player has chosen: rock
The computer has chosen: scissors
The player has won, good job!
Type 'e' to end this game or 'c' to continue: e
The player has chosen to end the game.
The player played 1 round.
Final Score - Player: 1, Computer: 0
There were 0 tie(s) in this game.
Thank you for playing!
```

## Conclusion
This Rock-Paper-Scissors game demonstrates key programming skills in Python:
- **Code Clarity**: Well-structured, modular code.
- **Logical Flow**: Efficient game logic for smooth gameplay.
- **Error Handling**: User-friendly error handling for a hassle-free experience.

Thank you for playing! Enjoy this example of simple, interactive Python programming.
