import string

def analyze_password(password):
    score = 0
    suggestions = []

    has_upper = any(char.isupper() for char in password)
    has_lower = any (char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if has_upper:
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if has_lower:
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if has_number:
        score += 1
    else:
        suggestions.append("Add numbers.")

    if has_special:
        score += 1
    else:
        suggestions.append("Add special characters.")


    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    return strength, suggestions