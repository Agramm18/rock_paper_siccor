print("\n")  # Print a new line for better readability in the output
import random  # Import the random module to enable random choice selection

class Game:  # Define the Game class, which contains all the game logic and player interaction
    def __init__(self):  # Initialize the Game class with default attributes
        self.computer_final_scores = []  # List to store the computer's scores at the end of each game
        self.player_final_scores = []  # List to store the player's scores at the end of each game
        self.final_round = []  # List to store the final round number
        self.player_points = 0  # Counter for the player's points
        self.computer_points = 0  # Counter for the computer's points
        self.ties = 0  # Counter for the number of tied rounds
        self.round = 1  # Variable to keep track of the round number

    def play_game(self):  # Define the main method for executing game logic
        options = ("rock", "paper", "scissors")  # Define the available options for the game

        while True:  # Start an infinite loop until the player chooses to end the game
            try:
                if self.round == 1:  # Welcome message for the first round
                    print("Welcome to Round One! Let's have some fun with this game.")

                print(f"Choose one of the following: {options}")  # Display the available options to the player
                player_choice = input("Please choose 'rock', 'paper', or 'scissors' to continue: ").lower()  # Get player input, convert to lowercase for consistency
                computer_choice = random.choice(options)  # Randomly select an option for the computer

                # Validate player input to ensure it's valid
                if player_choice not in options:
                    print("\n")  # New line for readability
                    raise ValueError("Invalid input. Please type 'rock', 'paper', or 'scissors' to continue.")  # Error for invalid input

                # Display choices
                print(f"Player chose: {player_choice}")
                print(f"Computer chose: {computer_choice}")

                # Determine the outcome based on the player’s and computer's choices
                if player_choice == computer_choice:  # Check for a tie
                    print("Both players have chosen the same option, it's a tie.")
                    self.ties += 1  # Increment tie counter

                elif player_choice == "rock" and computer_choice == "scissors":
                    print("The player has won, good job!")
                    self.player_points += 1  # Add a point to the player's score

                elif player_choice == "scissors" and computer_choice == "paper":
                    print("The player has won, good job!")
                    self.player_points += 1  # Add a point to the player's score

                elif player_choice == "paper" and computer_choice == "rock":
                    print("The player has won, good job!")
                    self.player_points += 1  # Add a point to the player's score

                else:
                    print("The computer has won, better luck next time.")
                    self.computer_points += 1  # Add a point to the computer's score

                # Ask if the player wants to continue or end
                next_step = input("Type 'e' to end the game or 'c' to continue: ").lower()  # Capture decision

                # Validate input for next step
                if next_step not in ["e", "c"]:
                    print("\n")  # New line for readability
                    raise ValueError("Invalid input. Type 'e' to end or 'c' to continue.")  # Error for invalid next step

                elif next_step == "e":  # If player chooses to end
                    print("\n")
                    print("Game Over.")
                    print(f"Rounds played: {self.round}")
                    self.player_final_scores.append(self.player_points)  # Record player's final score
                    self.computer_final_scores.append(self.computer_points)  # Record computer's final score
                    print(f"Final Score - Player: {self.player_points}, Computer: {self.computer_points}")  # Display final scores

                    if self.ties == 0:
                        print("No ties in this game.")  # Indicate if there were no ties
                    else:
                        print(f"Ties: {self.ties} time(s)")  # Display the number of ties

                    # Determine final winner
                    if self.player_points > self.computer_points:
                        print("Congratulations! The Player is the final winner.")
                    elif self.player_points < self.computer_points:
                        print("Computer wins the game! Better luck next time.")
                    else:
                        print("It's a draw! Both have the same score.")

                    print("Thank you for playing!")  # End message
                    break  # End the game loop

                else:  # If player continues
                    print("Moving to the next round...")
                    self.round += 1  # Increment round counter
                    print(f"Current Score - Player: {self.player_points}, Computer: {self.computer_points}\n")  # Display current score
                    print(f"Round {self.round} begins!")
                    
            except ValueError as error:  # Handle invalid input
                print(error)  # Display error message
                print("Please follow the instructions and try again.")  # Reminder for valid input

# Create an instance of the Game class and start the game
game_instance = Game()
game_instance.play_game()
