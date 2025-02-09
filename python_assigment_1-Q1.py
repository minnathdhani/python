"""
    Checks the strength of a password based on the following criteria:
    - Minimum length of 8 characters
    - Contains both uppercase and lowercase letters
    - Contains at least one digit (0-9)
    - Contains at least one special character (e.g., !, @, #, $, %)
    """
import re

def check_password_strength(password: str) -> bool:
    
    if (len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
        return True
    return False

def main():
    while True:
        password = input("Enter your password: ")
        if check_password_strength(password):
            print("Your Password is Strong.")
            break
        else:
            print("Your password is weak. Please make sure it meets the following criteria:")
            print("*At least 8 characters long")
            print("*Contains both uppercase[A-Z] and lowercase letters[a-z]")
            print("*Contains at least one digit (0-9)")
            print("*Contains at least one special character (e.g., !, @, #, $, %)")


if __name__ == "__main__":
    main()
