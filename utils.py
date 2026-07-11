Create a file named utils.py for password validation and security functions:
import re


# Password strength validation
def validate_password(password):
    """
    Checks password strength:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number
    - At least one special character
    """

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[!@#$%^&*]", password):
        return False

    return True


# Email validation
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        return True

    return False


# Remove unwanted spaces
def clean_input(data):
    return data.strip()
Purpose of utils.py:
✅ Password strength checking
✅ Email format validation
✅ Input cleaning
✅ Improves security of login system