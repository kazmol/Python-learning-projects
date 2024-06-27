import random 
import string

def generate_password(min_lenght, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char.isdigit():
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd

min_lenght = int(input("Enter min lenght: "))
has_numbers = input("Do you want numbers? (y/n): ").lower() == "y"
has_special = input("Do you want special characters? (y/n): ").lower() == "y"

pwd = generate_password(min_lenght, has_numbers, has_special)

print("Your password is: " + pwd)