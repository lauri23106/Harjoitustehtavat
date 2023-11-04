from random import randint

# Step 1: Create an empty list named thrownDiceNumbers
thrownDiceNumbers = []

# Step 2: Generate 5 random numbers and add them to the list
for _ in range(5):
    random_number = randint(1, 6)  # Generates a random number between 1 and 6 (inclusive)
    thrownDiceNumbers.append(random_number)

# Step 3: Print the whole list
print("List of thrown dice numbers:", thrownDiceNumbers)

# Step 4: Calculate and print the sum of the list values
sum_of_numbers = sum(thrownDiceNumbers)
print("Sum of the numbers:", sum_of_numbers)

# Step 5: Print the highest value in the list
highest_value = max(thrownDiceNumbers)
print("Highest value:", highest_value)
