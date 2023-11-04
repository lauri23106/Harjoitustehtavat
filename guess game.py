# The name to guess
correct_name = "John"

# Start the game
while True:
    # Ask the user to enter a guess
    user_guess = input("Guess the name: ")

    # Check if the user's guess is correct
    if user_guess == correct_name:
        print("Congratulations! You guessed the correct name.")
        break  # Exit the loop if the guess is correct
    else:
        print("Incorrect guess. Try again.")
