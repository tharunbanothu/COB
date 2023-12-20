#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install cryptography


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[25]:


import hashlib
import os
import json

PASSWORDS_FILE = "passwords.json"
HASH_ALGORITHM = hashlib.sha256

def get_master_password():
    master_password = input("Enter master password: ")
    return HASH_ALGORITHM(master_password.encode()).hexdigest()

def encrypt(password, key):
    cipher = hashlib.pbkdf2_hmac(HASH_ALGORITHM().name, password.encode(), key.encode(), 100000)
    return cipher.hex()

def decrypt(cipher, key):
    password = hashlib.pbkdf2_hmac(HASH_ALGORITHM().name, cipher.encode(), key.encode(), 100000)
    return password.decode()

def add_password(master_password):
    service = input("Enter service name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open(PASSWORDS_FILE, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = {}

    encrypted_password = encrypt(password, master_password)
    data[service] = {
        "username": username,
        "encrypted_password": encrypted_password
    }

    with open(PASSWORDS_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("Password added successfully!")

def delete_password(master_password):
    service = input("Enter service name: ")

    try:
        with open(PASSWORDS_FILE, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Empty or invalid JSON file.")
        return

    if service in data:
        del data[service]

        with open(PASSWORDS_FILE, "w") as file:
            json.dump(data, file, indent=4)

        print("Password deleted successfully!")
    else:
        print("Password for service '{}' not found.".format(service))

def view_password(master_password):
    service = input("Enter service name: ")

    try:
        with open(PASSWORDS_FILE, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Empty or invalid JSON file.")
        return

    if service in data:
        encrypted_password = data[service]["encrypted_password"]
        password = decrypt(encrypted_password, master_password)
        print("Username: {}".format(data[service]["username"]))
        print("Password: {}".format(password))
    else:
        print("Password for service '{}' not found.".format(service))

def main():
    # Create passwords file if not exists
    if not os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, "w") as file:
            file.write("{}")  # Empty JSON object

    master_password = get_master_password()

    while True:
        print("1. Add password")
        print("2. Delete password")
        print("3. View password")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_password(master_password)
        elif choice == "2":
            delete_password(master_password)
        elif choice == "3":
            view_password(master_password)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:






# In[ ]:




