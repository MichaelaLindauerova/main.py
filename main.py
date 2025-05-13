"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michaela Lindauerová
email: apricotsa@gmail.com
"""
# Import required libraries:
import random

# Definition of required functions:

# Function to generate a random 4-digit number with unique digits
def generate_secret_number():
    number = random.sample(range(0, 10), k=4)
    while number[0] == 0:
        number = random.sample(range(0, 10), k=4)
    return number

# Function to validate the user input
def validate_input(user_input):
    if not user_input.isnumeric():
        print("Input contains non-numeric characters. Please enter 4 digits.")
        return False
    elif (len(user_input) < 4) or (len(user_input) > 4):
        print("Invalid number of characters. Please enter exactly 4 digits.")
        return False
    elif user_input[0] == "0":
        print("The number must not start with 0.")
        return False
    elif len(set(user_input)) != 4:
        print("The number contains duplicate digits. Please enter 4 unique digits.")
        return False
    else:
        return True

# Function to convert user input to a list of integers
def convert_input_to_list(user_input):
    converted_input = []
    for char in user_input:
        converted_input.append(int(char))
    return converted_input

# Function to calculate number of cows
def count_cows(guess, secret_number):
    cows = 0
    for i in range(len(guess)):
        if (guess[i] in secret_number) and (guess[i] != secret_number[i]):
            cows += 1
    return cows

# Function to calculate number of bulls
def count_bulls(guess, secret_number):
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            bulls += 1
    return bulls

# Function to evaluate and return bulls/cows message
def overall_evaluation(guess, secret_number):
    bulls = count_bulls(guess, secret_number)
    cows = count_cows(guess, secret_number)

    if bulls == 1:
        bull_text = f"{bulls} bull"
    else:
        bull_text = f"{bulls} bulls"

    if cows == 1:
        cow_text = f"{cows} cow"
    else:
        cow_text = f"{cows} cows"

    return f"{bull_text}, {cow_text}"

# Local variables
separator = "-" * 60
secret_number = generate_secret_number()
guess_count = 0

# Bulls and Cows game
print(
    f"{separator}\nHi there!\n{separator}\n"
    f"I've generated a random 4 digit number for you.\n"
    f"Let's play a bulls and cows game.\n{separator}\n"
    f"Enter a number:\n{separator}"
)

while True:
    user_input = input()
    if validate_input(user_input):
        guess = convert_input_to_list(user_input)
        guess_count += 1
        print(overall_evaluation(guess, secret_number))
        if count_bulls(guess, secret_number) == 4:
            print(f"Correct, you've guessed the right number in {guess_count} guesses!")
            break
