import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)

# Maximum number of attempts
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if guess is out of range
    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
        continue

    # Reduce attempt for a valid guess
    attempts -= 1

    if guess > secret_number:
        print("Your guess is too high.")

    elif guess < secret_number:
        print("Your guess is too low.")

    else:
        print("Congratulations! You guessed the correct number.")
        break

else:
    print("Better luck next time!")

    # Ask the user to enter a number
number = int(input("Enter a number: "))

# Generate multiplication table from 1 to 10
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)

    # Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Get weight and height from the user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI using the function
bmi = calculate_bmi(weight, height)

# Display the BMI
print("Your BMI is:", bmi)