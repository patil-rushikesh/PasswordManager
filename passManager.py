import os
import json
import getpass
import random
import string
from cryptography.fernet import Fernet

# Class for encryption and decryption
class PasswordEncryptor:
    def __init__(self, key_file='key.key'):
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.generate_key()
        self.key = self.load_key()

    # Generates and saves a new encryption key
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as file:
            file.write(key)

    # Loads the encryption key from file
    def load_key(self):
        with open(self.key_file, 'rb') as file:
            return file.read()

    # Encrypts a password
    def encrypt(self, password):
        fernet = Fernet(self.key)
        return fernet.encrypt(password.encode()).decode()

    # Decrypts a password
    def decrypt(self, encrypted_password):
        fernet = Fernet(self.key)
        return fernet.decrypt(encrypted_password.encode()).decode()

# Password Manager class for handling password operations
class PasswordManager:
    def __init__(self, data_file='passwords.json'):
        self.data_file = data_file
        self.encryptor = PasswordEncryptor()
        self.data = self.load_data()

    # Load data from the JSON file
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    # Save data to the JSON file
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    # Add a new password
    def add_password(self):
        account = input("Enter account name: ")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        encrypted_password = self.encryptor.encrypt(password)
        self.data[account] = {'username': username, 'password': encrypted_password}

        self.save_data()
        print("Password added successfully.")

    # View saved passwords (hidden)
    def view_passwords(self):
        if not self.data:
            print("No saved passwords.")
            return

        for account, details in self.data.items():
            print(f"Account: {account}, Username: {details['username']}")

    # Reveal a password after master password authentication
    def reveal_password(self):
        account = input("Enter account name: ")
        if account in self.data:
            master_password = getpass.getpass("Enter master password to reveal the password: ")
            if master_password == "masterpass":  # Simple authentication check
                encrypted_password = self.data[account]['password']
                decrypted_password = self.encryptor.decrypt(encrypted_password)
                print(f"Password for {account}: {decrypted_password}")
            else:
                print("Incorrect master password.")
        else:
            print("Account not found.")

    # Delete a saved password
    def delete_password(self):
        account = input("Enter account name to delete: ")
        if account in self.data:
            confirm = input(f"Are you sure you want to delete the password for {account}? (yes/no): ")
            if confirm.lower() == 'yes':
                del self.data[account]
                self.save_data()
                print("Password deleted.")
        else:
            print("Account not found.")

    # Update an existing password
    def update_password(self):
        account = input("Enter account name to update password: ")
        if account in self.data:
            new_password = getpass.getpass("Enter new password: ")
            encrypted_password = self.encryptor.encrypt(new_password)
            self.data[account]['password'] = encrypted_password
            self.save_data()
            print("Password updated successfully.")
        else:
            print("Account not found.")

    # Generate a strong random password
    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print(f"Generated password: {password}")
        return password

# Main function to interact with the user
def main():
    manager = PasswordManager()
    
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Reveal Password")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Generate Random Password")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_password()
        elif choice == '2':
            manager.view_passwords()
        elif choice == '3':
            manager.reveal_password()
        elif choice == '4':
            manager.update_password()
        elif choice == '5':
            manager.delete_password()
        elif choice == '6':
            length = int(input("Enter password length (default is 12): ") or 12)
            manager.generate_password(length)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
