import random
import string

# перевірка на існування вписаного числа
def input_length():
    try:
        leng = int(input("\nPlease enter the desired password length: "))
        # minimal length
        if leng <= 3:
            print("Password is too short! Minimal length should be at least 4 characters!")
            reinit()
        return leng
    except:
        print("\nYou may have entered a letter instead of a number or you may not have entered a number at all. Please enter a password length of 4 characters or more")
        reinit()

def password_generation(leng):
    uppercase_letter = string.ascii_uppercase
    lowercase_letter = string.ascii_lowercase
    digit = string.digits
    special_char = string.punctuation

    pasw = [random.choice(uppercase_letter), random.choice(lowercase_letter), random.choice(digit), random.choice(special_char)]

    remaining_length = leng - 4
    pasw+= random.choices(uppercase_letter + lowercase_letter + digit + special_char, k=remaining_length)

    # Shuffle the characters in the password
    random.shuffle(pasw)

    # Convert the list of characters to a string
    pasw = ''.join(pasw)

    return pasw

    #special_character = ['!', '@', '#', '$', '%', '^', '&', '*']

    #pasw.insert(randint(0, leng-1), choice(special_character))
    #pasw.append(choice(special_character))
    
    #print(choice(special_character))

def reinit():
    answer = input("Do you want new generation? (Y/N): ");

    if answer.lower() == "y":
        main();
    elif answer.lower() == "n":
        print("\nGoodbye!")
    else:
        print("\nInvalid input! Please enter Y or N.")
        reinit()

def main():
    print("Welcome to the Linux User Password Generator")
    leng = input_length()
    pasw = password_generation(leng)
    print("Generated password:", pasw)
    reinit()

main()
