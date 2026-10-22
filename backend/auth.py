
import re
import hashlib

users = {}


def hash_password(password):
    """Hash a password before storing it."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(name, email, student_id, password):
    """Register a user after validating the email and hashing the password."""

    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(email_pattern, email):
        return "Invalid email format"

    if email in users:
        return "Email already registered"

    users[email] = {
        "name": name,
        "email": email,
        "student_id": student_id,
        "password": hash_password(password)
    }

    return "Registration successful"


def login_user(email, password):
    """Verify the user's email and password and return the login result."""

    if email in users and users[email]["password"] == hash_password(password):
        return "Login successful"

    return "Invalid email or password"

