"""
Login Validation Module
"""

import re


def validate_username(username):
    if len(username) < 5:
        return False
    return True


def validate_password(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    return True


def login(username, password):
    if not validate_username(username):
        return "Invalid username"

    if not validate_password(password):
        return "Weak password"

    return "Login Successful"


def run_test():
    user = "student1"
    pwd = "Password123"

    result = login(user, pwd)
    print(result)


if __name__ == "__main__":
    run_test()
