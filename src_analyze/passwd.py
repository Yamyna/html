import sys

def check_password_in_rockyou(password, file_path):
    """
    Checks if the given password is present in the specified RockYou password list file.

    Args:
        password (str): The password to check.
        file_path (str): The path to the RockYou password list file.

    Returns:
        bool: True if the password is found in the file, False otherwise.
    """
    with open('/tmp/scan_result_passwd.txt', 'a') as f:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                for line in file:
                    if line.strip() == password:
                        return True
            return False
        except FileNotFoundError:
            f.write(f"The file does not exist.")
            return False

def contains_uppercase(password):
    """
    Checks if the given password contains at least one uppercase letter.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains an uppercase letter, False otherwise.
    """
    for char in password:
        if char.isupper():
            return True
    return False

def contains_lowercase(password):
    """
    Checks if the given password contains at least one lowercase letter.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains a lowercase letter, False otherwise.
    """
    for char in password:
        if char.islower():
            return True
    return False

def contains_digit(password):
    """
    Checks if the given password contains at least one digit.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains a digit, False otherwise.
    """
    for char in password:
        if char.isdigit():
            return True
    return False

def contains_special_character(password):
    """
    Checks if the given password contains at least one special character.

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password contains a special character, False otherwise.
    """
    special_characters = "!@#$%^&*()-_+=<>?/|\\{}[]~`"
    for char in password:
        if char in special_characters:
            return True
    return False

def has_minimum_length(password, length=12):
    """
    Checks if the given password meets the minimum length requirement.

    Args:
        password (str): The password to check.
        length (int): The minimum length required. Default is 12.

    Returns:
        bool: True if the password meets the minimum length, False otherwise.
    """
    return len(password) >= length

if __name__ == "__main__":
    with open('/tmp/scan_result.txt', 'a') as f:
        if len(sys.argv) != 2:
            f.write("Usage: python check_password.py <password>")
        else:
            password = sys.argv[1]
            file_path_1 = '/script/script_LightningMalware/src_analyze/rockyou_1.txt'
            file_path_2 = '/script/script_LightningMalware/src_analyze/rockyou_2.txt'
            
            f.write("------------- CHECK PASSWORD ------------\n")
            f.write("\nPassword: " + password)
            if has_minimum_length(password):
                f.write("\n✓ 12 characters")
            else:
                f.write("\n✗ 12 characters")
            if contains_uppercase(password):
                f.write("\n✓ Uppercase letter")
            else:
                f.write("\n✗ Uppercase letter")
            if contains_lowercase(password):
                f.write("\n✓ Lowercase letter")
            else:
                f.write("\n✗ Lowercase letter")
            if contains_digit(password):
                f.write("\n✓ Digit")
            else:
                f.write("\n✗ Digit")
            if contains_special_character(password):
                f.write("\n✓ Special character")
            else:
                f.write("\n✗ Special character")

            if check_password_in_rockyou(password, file_path_1):
                f.write("\n✗ in rockyou")
            elif check_password_in_rockyou(password, file_path_2):
                f.write("\n✗ in rockyou")
            else:
                f.write("\n✓ in rockyou")
            
            f.write("\n\n'rockyou' is a well-known list of common passwords that were exposed in a data breach. It is often used by security professionals to test the strength of passwords. If your password is found in the 'rockyou' list, it is considered highly insecure.")

            if has_minimum_length(password) and contains_uppercase(password) and contains_lowercase(password) and contains_digit(password) and contains_special_character(password) and not check_password_in_rockyou(password, file_path_1) and not check_password_in_rockyou(password, file_path_2) :
                f.write("\n\n✓ is safe")
            else :
                f.write("\n\n✗ is safe")
