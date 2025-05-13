"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michaela Lindauerová
email: apricotsa@gmail.com
"""
# Importing a library
import string

# Given variables
registered = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# User login
switch = True
while switch == True:
    entered_name = input("Username:")
    name = entered_name.lower()
    if name in registered.keys():
        entered_password = input("Password:")
        if entered_password == registered[name]:
            switch = False
        else:
                print("Incorrect password, terminating the program...")
    else:
        print("Unregistered user, terminating the program...")

# Continue to the program
# User greeting and selection of texts for analysis
separator = "-" * 50
numbers_of_texts = len(TEXTS)
print(separator)
print(f"Welcome to the app {name.title()}!")
print(separator)
print(f"We have {numbers_of_texts} texts to be analyzed.")
print(separator)
for number_of_text, text in enumerate(TEXTS, start=1):
     print(f"{number_of_text}: {text}")
print(separator)

while True:
    number_of_choosen_text = input(f"Enter a number btw. 1 and {numbers_of_texts} to select:")
    if not number_of_choosen_text.isnumeric():
        print("Invalid input!")
        continue
    number_of_choosen_text = int(number_of_choosen_text)
    if not 1 <= number_of_choosen_text <= numbers_of_texts:
        print("Number out of range.")
        continue
    else:  
        break 

choosen_text = TEXTS[number_of_choosen_text - 1]

# Variables for analysis output
words = len(choosen_text.split())
titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
sum_of_numbers = 0

# Text analysis
for word in choosen_text.split():
    if word.strip(string.punctuation).istitle():
        titlecase += 1
    if word.strip(string.punctuation).isupper():
        uppercase += 1
    if word.strip(string.punctuation).islower():
        lowercase += 1
    if word.strip(string.punctuation).isnumeric():
        numeric += 1
        sum_of_numbers += int(word.strip(string.punctuation))   

# Output from the analysis
print(f"There are {words} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {sum_of_numbers}")
print(separator)

# Simple bar chart
chart = {}
for word in choosen_text.split():  
    character_count = len(word.strip(string.punctuation))
    if character_count in chart:
        chart[character_count] += 1
    else:
        chart[character_count] = 1

# Bar Chart - analysis output
alignment_width = max(chart.values())
print("LEN |","OCCURRENCES".ljust(alignment_width),"| NR.")
print(separator)
for characters, value in sorted(chart.items()):
    print(str(characters).rjust(3),"|", ("*" * value).ljust(alignment_width), "|", str(value))







