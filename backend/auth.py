users = {}

def register_user(name, email, student_id, password):
    if email in users:
        return "Email already registered"

    users[email] = {
        "name": name,
        "email": email,
        "student_id": student_id,
        "password": password
    }

    return "Registration successful"


def login_user(email, password):
    if email in users and users[email]["password"] == password:
        return "Login successful"

    return "Invalid email or password"
