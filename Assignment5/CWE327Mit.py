"""
Hiren Shah
SDEV 325 7380
4/20/2021
Professor Matthew L. Brown, Ph.D
Demonstrating Porous Defenses Final
CWE327 - Mitigated
"""
from passlib.hash import sha256_crypt

alphabet = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"the encoded text is {cipher_text}")
  
  hash_pass = sha256_crypt.hash(cipher_text) 
  print(hash_pass)
  
encrypt(text, shift)