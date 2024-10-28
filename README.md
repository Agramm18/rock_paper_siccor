# Rock-Paper-Scissors Game

This repository contains a Python-based, interactive Rock-Paper-Scissors game. Designed with simplicity and user experience in mind, the game offers an engaging way to practice basic Python skills and understand game logic. This project is ideal for anyone looking to explore Python programming through a practical example, including private users or employers assessing coding style, error handling, and user interaction techniques.

## Features

- **Interactive Gameplay**: The game allows players to go multiple rounds against a computer opponent, with choices between rock, paper, and scissors.
- **Score Tracking**: Each round’s score is recorded, displaying total wins, losses, and ties by the game’s end.
- **Error Handling**: The program handles user inputs carefully, ensuring only valid choices are accepted to maintain smooth gameplay.
- **User-Friendly Interface**: With clear prompts and feedback, this project is designed to be engaging and accessible, even to those unfamiliar with Python.

## How It Works

- **Choice Options**: The player is prompted to choose between "rock," "paper," or "scissors." The computer's choice is randomly selected.
- **Game Logic**: The program evaluates each choice combination and determines the winner based on classic Rock-Paper-Scissors rules.
- **Endgame Options**: After each round, players can choose to continue or end the game, with a final score summary displayed upon exiting.

## Code Highlights

- **Object-Oriented Design**: The game is structured around a `Game` class, making the code modular, organized, and easier to extend.
- **Input Validation**: Handles incorrect inputs gracefully with appropriate error messages.
- **Round Management**: The game tracks rounds and scores dynamically, offering real-time feedback between rounds.

## Usage

1. **Install Python**: Ensure Python 3.x is installed on your machine.
2. **Clone the Repository**: Clone the repository to your local machine.
3. **Run the Game**: Execute the game script in the terminal using:
   ```bash
   python game.py
   ```
4. **Enjoy the Game**: Follow the prompts to play.

## Example Output

```
Welcome to round one! Have fun with this game.
You can choose between ('rock', 'paper', 'scissor')
Please choose between these options to continue the game: rock
The player has chosen: rock
The computer has chosen: scissors
The player has won, good job!
Type 'e' to end this game or 'c' to continue: e
The player has chosen to end the game.
The player played 1 rounds
Final Score - Player: 1, Computer: 0
There were 0 tie(s) in this game.
Thank you for playing!
```

## Future Enhancements

- **Additional Game Modes**: Implement options for best of three, five, or custom rounds.
- **User Profiles**: Track scores across sessions.
- **Advanced Moves**: Include other moves such as "lizard" and "Spock" for expanded gameplay.
