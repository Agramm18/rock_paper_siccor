print("\n")  # Print a new line for better readability in the output
import random  # Import the random module to allow random choice selection

class Game:  # Define the Game class, which contains all the game logic and player interaction
    def __init__(self):  # Initialize the Game class with default attributes
        self.computer_final_scores = []  # List to store the computer's scores at the end of each game
        self.player_final_scores = []  # List to store the player's scores at the end of each game
        self.final_round = []  # Stores the final round number
        self.player_points = 0  # Counter to track the player's points
        self.computer_points = 0  # Counter to track the computer's points
        self.ties = 0  # Counter for the number of tied rounds
        self.round = 1  # Variable to keep track of the round number

    def play_game(self):  # Define the main method for executing game logic
        options = ("rock", "paper", "scissor")  # Define the available options for the game as a tuple

        while True:  # Start an infinite loop that will run until the player chooses to end the game
            try:
                if self.round < 2:  # Check if it's the first round
                    print("Welcome to round one! Have fun with this game.")  # Friendly welcome message for the player

                print(f"You can choose between {options}")  # Display the available options to the player
                player_choice = input("Please choose between these options to continue the game: ").lower()  # Prompt player for their choice, converting input to lowercase for consistency
                computer_choice = random.choice(options)  # Randomly select an option for the computer

                # Validate player's input to ensure it's one of the allowed choices
                if player_choice not in options:
                    print("\n")  # Add a new line for readability
                    raise ValueError("Invalid input, please type 'rock', 'paper', or 'scissor' to continue.")  # Raise an error for invalid input

                # Display both player and computer choices
                print(f"The player has chosen: {player_choice}")
                print(f"The computer has chosen: {computer_choice}")

                # Determine the outcome based on the player’s and computer's choices
                if player_choice == computer_choice:  # Check for a tie
                    print("Both players have chosen the same option, it's a tie.")
                    self.ties += 1  # Increment the tie counter

                elif player_choice == "rock" and computer_choice == "scissor":
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

                # Prompt player to either end the game or continue playing
                next_step = input("Type 'e' to end this game or 'c' to continue: ").lower()  # Capture player decision

                # Validate input for next step to ensure only 'e' or 'c' is accepted
                if next_step not in ["e", "c"]:
                    print("\n")  # Add a new line for readability
                    raise ValueError("Invalid input, please type 'e' to end or 'c' to continue.")  # Raise error for invalid next-step input

                elif next_step == "e":  # Check if the player chose to end the game
                    print("\n")
                    print("The player has chosen to end the game.")
                    print(f"The player played {self.round} rounds")  # Display total rounds played
                    self.player_final_scores.append(self.player_points)  # Record player's final score
                    self.computer_final_scores.append(self.computer_points)  # Record computer's final score
                    print(f"Final Score - Player: {self.player_points}, Computer: {self.computer_points}")  # Display final scores
                    print(f"There were {self.ties} tie(s) in this game.")  # Display the number of ties

                    if self.ties < 1:
                        print("In this round, there were no ties.")  # Indicate if there were no ties

                    print("Thank you for playing!")  # Thank the player for participating
                    break  # Exit the loop and end the game

                else:  # If the player chose to continue
                    print("The player has chosen to play another round.")
                    print("Good luck in the next round!")
                    print("\n")
                    print("Welcome to the next round.")
                    self.round += 1  # Increment the round number
                    print(f"Welcome to round {self.round}")
                    print(f"Current Score - Player: {self.player_points}, Computer: {self.computer_points}")  # Show current score
                    continue  # Restart the game loop for the next round

            except ValueError as error:  # Handle invalid input cases
                print(error)  # Display error message
                print("Please follow the instructions and try again.")  # Friendly reminder to provide valid input

# Create an instance of the Game class and start the game by calling play_game
game_instance = Game()
game_instance.play_game()
