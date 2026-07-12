#password strength checker
import re

def check_password_strength(password):
    #function to check the strength of a password.

    if len(password) < 8:
        return "Weak: Password must be at least 8 charachters long"
    
    if not any(char.isdgit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    return "Strong: Your password is secure!"

def password_checker():
    #main function to take user input and check password strength

    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("\nEnter your password (or type 'exit' to quit)")

        if password.lower() == "exit":
            print("Thank you for using the password strength checker")
            break
        result = check_password_strength(password)
        print(result)

# run the password checker tool
if __name__ == "__main__":
   password_checker()