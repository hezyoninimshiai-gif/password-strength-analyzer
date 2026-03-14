import re

# Common weak passwords (sample database)
weak_passwords = [
    "password",
    "123456",
    "123456789",
    "qwerty",
    "abc123",
    "password123",
    "admin",
    "letmein"
]

def check_password_strength(password):
    score = 0
    suggestions = []
    if password.lower() in weak_passwords:
        return 0, ["This password appears in a common password list. Choose a stronger password."]
    

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length (at least 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions


def main():
    password = input("Enter password to analyze: ")

    score, suggestions = check_password_strength(password)

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)
    else:
        print("Your password is strong!")


if __name__ == "__main__":
    main()