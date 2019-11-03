# Brett Roach
# brettmroach@umail.ucsb.edu
# 6907380

from string import ascii_lowercase
from string import ascii_uppercase


def createAlphabet():
    alphabet=ascii_lowercase + ascii_uppercase + " ,.-~#"
    return alphabet


#if "key" is an integer
def encryptCaesarCipher(plainText, key):
    alphabet = createAlphabet()
    if type(plainText) != str:
        return "Invalid text"
    else:
        if type(key) == int:
            encryptedText = str()
            while key < 0:
                key = key*(-1)
            while key > len(alphabet):
                key = key % len(alphabet)
            for char in plainText:
                if char in alphabet:
                    x = alphabet.find(char)
                    encryptedText += alphabet[x-len(alphabet)+key]
                else:
                    encryptedText += char
            return encryptedText
        else:
            return "Invalid key"


#if "key" is an integer
def decryptCaesarCipher(plainText, key):
    alphabet = createAlphabet()
    if type(plainText) != str:
        return "Invalid text"
    else:
        if type(key) == int:
            decryptedText = str()
            while key < 0:
                key = key*(-1)
            while key > len(alphabet):
                key = key % len(alphabet)
            for char in plainText:
                if char in alphabet:
                    x = alphabet.find(char)
                    decryptedText += alphabet[x-key]
                else:
                    decryptedText += char
            return decryptedText
        else:
            return "Invalid key"



'''
#if "key" is an entire alphabet
def encryptCaesarCipher(plainText, key):
    alphabet = createAlphabet()
    if type(plainText) != str:
        return "Invalid text"
    else:
        if type(key) == str:
            if len(key) == len(alphabet):
                encryptedText = str()
                for char in plainText:
                    if char in alphabet:
                        x = alphabet.find(char)
                        encryptedText += key[x]
                    else:
                        encryptedText += char
                return encryptedText
            else:
                return "Invalid key"
        else:
            return "Invalid key"

#if "key" is an entire alphabet
def decryptCaesarCipher(plainText, key):
    alphabet = createAlphabet()
    if type(plainText) != str:
        return "Invalid text"
    else:
        if type(key) == str:
            if len(key) == len(alphabet):
                decryptedText = str()
                for char in plainText:
                    if char in key:
                        x = key.find(char)
                        decryptedText += alphabet[x]
                    else:
                        decryptedText += char
                return decryptedText
            else:
                return "Invalid key"
        else:
            return "Invalid key"
'''

def createBinKeyFromKey(key):
    if key >= 0:
        binKey = bin(key)[2:len(bin(key))]
        return binKey
    else:
        binKey = bin(key)[3:len(bin(key))]
        return binKey

def encryptCS8Cipher(plainText, key):
    alphabet = createAlphabet()
    binKey = createBinKeyFromKey(key)
    if type(plainText) != str:
        return "Invalid text"
    elif type(key) != int:
        return "Invalid key"
    else:
        encryptedText = str()
        while key < 0:
            key = key*(-1)
        while key > len(alphabet):
            key = key % len(alphabet)
        for i in range(len(plainText)):
            x = i
            while x >= len(binKey):
                x = x % len(binKey)
            if plainText[i] in alphabet:
                y = alphabet.find(plainText[i])
                if binKey[x] == "1":
                    encryptedText += alphabet[y-len(alphabet)+key]
                elif binKey[x] == "0":
                    encryptedText += alphabet[y-key]
            else:
                encryptedText += plainText[i]
        return encryptedText

def decryptCS8Cipher(plainText, key):
    alphabet = createAlphabet()
    binKey = createBinKeyFromKey(key)
    if type(plainText) != str:
        return "Invalid text"
    elif type(key) != int:
        return "Invalid key"
    else:
        decryptedText = str()
        while key < 0:
            key = key*(-1)
        while key > len(alphabet):
            key = key % len(alphabet)
        for i in range(len(plainText)):
            x = i
            while x >= len(binKey):
                x = x % len(binKey)
            if plainText[i] in alphabet:
                y = alphabet.find(plainText[i])
                if binKey[x] == "1":
                    decryptedText += alphabet[y-key]
                elif binKey[x] == "0":
                    decryptedText += alphabet[y-len(alphabet)+key]
            else:
                decryptedText += plaintext[i]
        return decryptedText
















