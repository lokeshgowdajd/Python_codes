# auth.py

def login(username, password):
    if username == "admin" and password == "admin":
        return "token123"
    else:
        return None
