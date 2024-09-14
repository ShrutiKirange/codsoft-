import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    # Define possible character sets based on the user's preferences
    char_set = ''
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("At least one character set must be selected!")

    # Generate the password using random.choice
    password = ''.join(random.choice(char_set) for _ in range(length))

    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    print(f"Generated password: {password}")