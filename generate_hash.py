import bcrypt

def hash_password(password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed.decode()

# Replace with your actual passwords
passwords = {
    "alexander": "alexandertiopan",
    "sabrina": "sabrinal123"
}

for user, pwd in passwords.items():
    print(f"{user}: {hash_password(pwd)}")
