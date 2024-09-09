# Password Manager

## Features

- **Add Password**: Securely add new passwords for various accounts. The password is encrypted before being saved.
- **View Saved Passwords**: List all saved passwords (passwords are hidden by default).
- **Reveal Password**: Reveal a password after authentication with a master password.
- **Delete Password**: Remove a saved password entry.
- **Update Password**: Update the password of an existing account and re-encrypt it.
- **Generate Random Password**: Create strong random passwords with customizable length.

## Libraries Used

- **`cryptography.fernet.Fernet`**: Provides encryption and decryption for passwords.
- **`json`**: Handles storing and loading password data in JSON format.
- **`os`**: Manages file and directory operations.
- **`getpass`**: Reads passwords securely from the terminal.
- **`random`** and **`string`**: Used for generating strong random passwords.

## Steps to Run the Code

1. **Install Dependencies**

   Ensure you have Python 3 installed. You need the `cryptography` library. Install it using pip:
   ```bash
   pip install cryptography

2. **Run the Code**

   ```bash
   python password_manager.py
