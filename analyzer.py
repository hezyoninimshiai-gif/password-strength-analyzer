import re
import math

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def estimate_crack_time(entropy):
    guesses_per_second = 1e9
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{round(seconds,2)} seconds"
    elif seconds < 3600:
        return f"{round(seconds/60,2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600,2)} hours"
    else:
        return f"{round(seconds/86400,2)} days"

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

common_patterns = [
    "1234",
    "abcd",
    "qwerty",
    "asdf",
    "password",
    "admin"
]

def check_password_strength(password):
    score = 0
    suggestions = []
    if password.lower() in weak_passwords:
        return 0, ["This password appears in a common password list. Choose a stronger password."]
    
    for pattern in common_patterns:
        if pattern in password.lower():
            suggestions.append("Avoid predictable patterns like '1234', 'abcd', or keyboard sequences")
            break

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
    entropy = calculate_entropy(password)
    print("Password Entropy:", entropy, "bits")
    print("Estimated crack time:", estimate_crack_time(entropy))

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)
    else:
        print("Your password is strong!")


if __name__ == "__main__":
    main()