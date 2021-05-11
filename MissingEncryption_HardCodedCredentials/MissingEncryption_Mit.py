"""
Hiren Shah
4/11/2021
MissingEncryption Mitigation
Purpose: This program actually encrypts the password by using the python library sha256_crypt, so if an attacker ran a
query to find the password file, they will only see the encrypted long password instead of the actual password.
"""

from passlib.hash import sha256_crypt

def saveUserToDatabase(username, password):
  with open('userDatabaseEncrypted.txt', 'a+') as file:
        file.seek(0) # moving the cursor to the begining of file
        for line in file:
            data = line.strip().split(",")
            if username == data[0]:
                return False  # since username exists

        hash_pass = sha256_crypt.hash(password)
        # write to end of file since username is unique
        file.write(username + "," + hash_pass + "\r")
        return True  # success
print("--- CWE 311 Mitigated Version ---")
print("== Register User Form == ")
username = input("Username: ")
password = input("Password: ")
if saveUserToDatabase(username, password):
  print("User created in database")
else:
  print("User exists in database")