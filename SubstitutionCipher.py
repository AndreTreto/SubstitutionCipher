global key
global alphabet
import random

values = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
word = input("Enter word: ")


def assign():
  global values
  for i in alphabet:
    values.append(i)


def encrypt(word):
  global encrypted
  global encryptedword
  encrypted = []
  encryptedword = ""
  for i in word:
    for k in values:
      if i == k:
        encrypted.append(key[values.index(k)])
        encryptedword = ''.join(str(j) for j in encrypted)


def decrypt(encrypted):
  global decrypted
  global decryptedword
  decrypted = []
  decryptedword = ""
  for k in encrypted:
    for i in key:
      if i == k:
        decrypted.append(values[key.index(i)])
        decryptedword = ''.join(str(j) for j in decrypted)


assign()
key = random.sample(values, len(values))
encrypt(word)
decrypt(encrypted)

print("The random key is: ", key)
print("The encrypted word is : " + encryptedword)
print("The decrypted word is : " + decryptedword)
