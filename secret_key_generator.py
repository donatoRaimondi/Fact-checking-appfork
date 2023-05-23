import secrets

secret_key = secrets.token_hex(16)

with open('secret_key.txt', 'w') as file:
    file.write(secret_key)