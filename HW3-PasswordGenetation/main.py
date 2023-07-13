import random
import string


class PasswordGenerator:
    """
    Password generator class that will generate random passwords based on certain criteria.

    length: an integer representing the length of the password (default: 8)
    include_uppercase: a boolean indicating whether to include uppercase letters in the password (default: True)
    include_lowercase: a boolean indicating whether to include lowercase letters in the password (default: True)
    include_digits: a boolean indicating whether to include digits in the password (default: True)
    include_special_chars: a boolean indicating whether to include special characters in the password (default: True)
    """
    def __init__(self,
                 length=8,
                 include_uppercase=True,
                 include_lowercase=True,
                 include_digits=True,
                 include_special_chars=True):
        """Initializes the attributes of the class."""
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generate_password(self):
        """Generates and returns a random password based on the specified criteria.
        The password should be a string of characters randomly chosen from the available character sets
        (uppercase letters, lowercase letters, digits, and special characters)."""
        character_set = ""
        if self.include_uppercase:
            character_set += string.ascii_uppercase
        if self.include_lowercase:
            character_set += string.ascii_lowercase
        if self.include_digits:
            character_set += string.digits
        if self.include_special_chars:
            character_set += string.punctuation

        # check for at least one character included
        if not character_set:
            print("At least one character set must be included.")
            reinit()

        password = random.choices(character_set, k=self.length)
        return "".join(password)


# Separate script that utilizes the PasswordGenerator class
def get_bool_input(prompt):
    """bool value change"""
    while True:
        try:
            return {"y": True, "n": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input. Please enter 'y' or 'n'.")


def get_int_input(length):
    """
    Set password length

    Parameters:
        length (int):

    Return:
        int: length of the password
    """
    while True:
        try:
            return int(input(length))
        except ValueError:
            print("Invalid input. Please enter an integer.")


def reinit():
    answer = input("\nDo you want new generation? (Y/N): ")

    if answer.lower() == "y":
        main()
    elif answer.lower() == "n":
        print("\nGoodbye!")
    else:
        print("\nInvalid input! Please enter Y or N.")
        reinit()


def main():
    print("Welcome to the Linux User Password Generator")
    length = get_int_input("\nEnter the desired password length: ")
    include_uppercase = get_bool_input("Include uppercase letters? (Y/N): ")
    include_lowercase = get_bool_input("Include lowercase letters? (Y/N): ")
    include_digits = get_bool_input("Include digits? (Y/N): ")
    include_special_chars = get_bool_input("Include special characters? (Y/N): ")
    password_generator = PasswordGenerator(length,
                                           include_uppercase,
                                           include_lowercase,
                                           include_digits,
                                           include_special_chars)
    print("\nGenerated password:", password_generator.generate_password())
    reinit()


main()
