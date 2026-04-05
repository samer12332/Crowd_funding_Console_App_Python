from storage import load_users, save_users
from validators import (
    is_valid_email,
    is_valid_egyptian_phone,
    passwords_match,
)
from utils import get_next_id


def register_user():
    users = load_users()

    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    if not first_name or not last_name:
        print("First name and last name are required.")
        return

    email = input("Email: ").strip().lower()
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    
    if any(user.get("email") == email for user in users):
        print("Email already exists.")
        return

    password = input("Password: ").strip()
    confirm_password = input("Confirm password: ").strip()
    if not passwords_match(password, confirm_password):
        print("Passwords do not match.")
        return

    mobile_phone = input("Egyptian mobile phone: ").strip()
    if not is_valid_egyptian_phone(mobile_phone):
        print("Invalid Egyptian phone number.")
        return

    new_user = {
        "user_id": get_next_id(users, "user_id"),
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile_phone": mobile_phone,
    }

    users.append(new_user)
    save_users(users)
    print("Registration successful.")


def login_user():
    users = load_users()

    email = input("Email: ").strip().lower()
    password = input("Password: ").strip()

    for user in users:
        if user.get("email") == email and user.get("password") == password:
            print("Login successful.")
            return user

    print("Invalid email or password.")
    return None
