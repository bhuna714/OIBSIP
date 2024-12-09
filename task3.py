import random
import string

def generate_password(length=12):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password includes at least one of each type of character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password with random characters
    password += random.choices(characters, k=length - 4)
    
    # Shuffle the password to make it more secure
    random.shuffle(password)
    
    # Convert the list to a string and return it
    return ''.join(password)

# Ask the user for the desired password length
length = int(input("Enter the desired password length (minimum 8): "))

if l