import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not re.search(r"[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Missing lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Missing number"
    if not re.search(r"[@$!%*?&]", password):
        return "Weak: Missing special character"
    return "Strong Password!"

password = input("Enter your password: ")
print(check_password_strength(password))