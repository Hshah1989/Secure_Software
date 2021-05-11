"""
Hiren Shah
4/11/2021
MissingEncryption Vulnerability
Purpose: This program asks user to enter username and password and stores it in the database .txt file and performs a check
if it already exists. The program does hash or encrypt any passwords, so an attacker can easily come in and user a malicious code to
find out what it is.
"""
# Missing Encryption of Sensitive Data (Vulnerability)

def saveUserToDatabase(username, password):
  with open('userDatabase.txt', 'a+') as file:
        file.seek(0) # moving the cursor to the begining of file
        for line in file:
            data = line.strip().split(",")
            if username == data[0]:
                return False  # since username exists

        file.write(username + "," + password + "\r")
        #hash_pass = sha256_crypt.hash(password)
        # write to end of file since username is unique
        #file.write(username + "," + hash_pass + "\r")
        return True  # success

print("== Register User Form == ")
username = input("Username: ")
password = input("Password: ")
if saveUserToDatabase(username, password):
  print("User created in database")
else:
  print("User exists in database")