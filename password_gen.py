import secrets
import string

# Define the length of the password
password_length = 12

# Define the characters to use for generating the password
alphabet = string.ascii_letters + string.digits + string.punctuation

# Generate the password using the secrets module
password = ''.join(secrets.choice(alphabet) for i in range(password_length))

# Print the generated password
print(password)