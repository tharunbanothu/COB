#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cryptography.fernet import Fernet

def generate_key():
    # Generate a new encryption key
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the encryption key from file
    with open("encryption_key.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(filename, key):
    # Read the file content
    with open(filename, "rb") as file:
        file_content = file.read()

    # Initialize the Fernet symmetric encryption object
    fernet = Fernet(key)

    # Encrypt the file content
    encrypted_content = fernet.encrypt(file_content)

    # Write the encrypted content back to the file
    with open(filename, "wb") as file:
        file.write(encrypted_content)

def decrypt_file(filename, key):
    # Read the encrypted file content
    with open(filename, "rb") as file:
        encrypted_content = file.read()

    # Initialize the Fernet symmetric encryption object
    fernet = Fernet(key)

    # Decrypt the file content
    decrypted_content = fernet.decrypt(encrypted_content)

    # Write the decrypted content back to the file
    with open(filename, "wb") as file:
        file.write(decrypted_content)

# Generate a new encryption key file
generate_key()

# Load the encryption key
encryption_key = load_key()

# Encrypt a file
encrypt_file("C:/Users/banot/OneDrive/Desktop/tharun.txt", encryption_key)
print("File encrypted successfully.")

# Decrypt the encrypted file
decrypt_file("C:/Users/banot/OneDrive/Desktop/tharun.txt", encryption_key)
print("File decrypted successfully.")


# In[ ]:




