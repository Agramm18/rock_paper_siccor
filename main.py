print("\n")  # Print a new line for better readability in the output
import random  # Import the random module to allow random choice selection

class Game:  # Define the Game class
    def __init__(self):  # Initialize the Game class
        self.computer_final_scores = []  # List to store the computer's scores at the end of each game
        self.player_final_scores = []  # List to store the player's scores at the end of each game
        self.player_points = 0  # Counter for player points
        self.computer_points = 0  # Counter for computer points

    def play_game(self):  # Define the main game logic method
        options = ("rock", "paper", "scissors")  # Define options for the game as a tuple

        while True:  # Loop to keep the game running until the player decides to end it
            try:
                print(f"You can choose between {options}")  # Display available options to the player
                player_choice = input("Please choose between these options to continue the game: ").lower()  # Prompt player for choice, make lowercase for consistency
                computer_choice = random.choice(options)  # Computer randomly selects an option

                # Validate player input
                if player_choice not in options:
                    print("\n")  # Add a new line for spacing
                    raise ValueError("Invalid input, please type 'rock', 'paper', or 'scissors' to continue.")  # Raise error for invalid input

                # Display player and computer choices
                print(f"The player has chosen: {player_choice}")
                print(f"The computer has chosen: {computer_choice}")

                # Determine the winner based on choices
                if player_choice == computer_choice:
                    print("Both players have chosen the same option, it's a tie.")
                    self.player_points = 0
                    self.computer_points = 0

                elif player_choice == "rock" and computer_choice == "scissors":
                    print("The player has won, good job!")
                    self.player_points += 1  # Increment player points

                elif player_choice == "scissors" and computer_choice == "paper":
                    print("The player has won, good job!")
                    self.player_points += 1  # Increment player points

                elif player_choice == "paper" and computer_choice == "rock":
                    print("The player has won, good job!")
                    self.player_points += 1  # Increment player points

                else:
                    print("The computer has won, better luck next time.")
                    self.computer_points += 1  # Increment computer points

                # Prompt player to continue or end the game
                next_step = input("Type 'e' to end this game or 'c' to continue: ").lower()

                # Validate continuation input
                if next_step not in ["e", "c"]:
                    print("\n")
                    raise ValueError("Invalid input, please type 'e' to end or 'c' to continue.")

                elif next_step == "e":
                    print("\n")
                    print("The player has chosen to end the game.")
                    self.player_final_scores.append(self.player_points)  # Append player's final score
                    self.computer_final_scores.append(self.computer_points)  # Append computer's final score
                    print(f"Final Score - Player: {self.player_points}, Computer: {self.computer_points}")
                    print("Thank you for playing!")
                    break  # Exit the game loop

                else:
                    print("The player has chosen to play another round.")
                    print("Good luck in the next round!")
                    print("\n")
                    print("Welcome to the next round.")
                    print(f"Current Score - Player: {self.player_points}, Computer: {self.computer_points}")

                    continue  # Restart the game loop for a new round

            except ValueError as error:  # Catch and handle invalid input
                print(error)  # Display the error message
                print("Please follow the instructions and try again.")  # Friendly reminder to follow instructions

# Create an instance of the Game class and start the game
game_instance = Game()
game_instance.play_game()
