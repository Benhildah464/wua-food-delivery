<<<<<<< HEAD
users = {}
=======
﻿import re
import hashlib

users = {}


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

>>>>>>> f8728ce (Address review feedback: add password hashing and email validation)

def register_user(name, email, student_id, password):
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
 HEAD
    user = users.get(email)

    if user and user["password"] == password:

    if email in users and users[email]["password"] == hash_password(password):
f8728ce (Address review feedback: add password hashing and email validation)
        return "Login successful"

    return "Invalid email or password"