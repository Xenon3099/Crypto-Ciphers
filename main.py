from Additive import AddCipher
from Multiplicative import Multicipher
from Affine import AffineCipher

def Additive():
    print "Additive Cipher Main Menu"
    print "1. Encrypt"
    print "2. Decrypt"
    print "3. Return"
    ch=input("Enter your choice: ")
    if ch==1:
        plain=raw_input("Enter the string to be encrypted : ")
        key=input("Enter the Encryption key : ")
        x=AddCipher()
        cipher=x.encrypt(plain,key)
        print "Encrypted using ",x.name," Cipher"
        print "The encrypted string is : ",cipher
    elif ch==2:
        cipher=raw_input("Enter the string to be decrypted : ")
        key=input("Enter the Decryption key : ")
        x=AddCipher()
        plain=x.decrypt(cipher,key)
        print "Decrypted using ",x.name," Cipher"
        print "The decrypted string is : ",plain
    else:
        print "Returning to Main Menu"

def Multiplicative():
    print "Multiplicative Cipher Main Menu"
    print "1. Encrypt"
    print "2. Decrypt"
    print "3. Return"
    ch=input("Enter your choice: ")
    if ch==1:
        plain=raw_input("Enter the string to be encrypted : ")
        while True:
            key=input("Enter the Encryption key : ")
            if key in [1,3,5,7,9,11,15,17,19,21,23,25]:
                break
            else:
                print "Please enter correct key"
        x=Multicipher()
        cipher=x.encrypt(plain,key)
        print "Encrypted using ",x.name," Cipher"
        print "The encrypted string is : ",cipher
    elif ch==2:
        cipher=raw_input("Enter the string to be decrypted : ")
        while True:
            key=input("Enter the Encryption key : ")
            if key in [1,3,5,7,9,11,15,17,19,21,23,25]:
                break
            else:
                print "Please enter correct key"
        x=Multicipher()
        plain=x.decrypt(cipher,key)
        print "Decrypted using ",x.name," Cipher"
        print "The decrypted string is : ",plain
    else:
        print "Returning to Main Menu"

def Affine():
    print "Affine Cipher Main Menu"
    print "1. Encrypt"
    print "2. Decrypt"
    print "3. Return"
    ch=input("Enter your choice: ")
    if ch==1:
        plain=raw_input("Enter the string to be encrypted : ")
        while True:
            key1=input("Enter the Encryption key 1 : ")
            if key1 in [1,3,5,7,9,11,15,17,19,21,23,25]:
                break
            else:
                print "Please enter correct key"
        key2=input("Enter the Encryption key 2 : ")
        x=AffineCipher()
        cipher=x.encrypt(plain,key1,key2)
        print "Encrypted using ",x.name," Cipher"
        print "The encrypted string is : ",cipher
    elif ch==2:
        cipher=raw_input("Enter the string to be decrypted : ")
        while True:
            key1=input("Enter the Encryption key 1 : ")
            if key1 in [1,3,5,7,9,11,15,17,19,21,23,25]:
                break
            else:
                print "Please enter correct key"
        key2=input("Enter the Encryption key 2 : ")
        x=AffineCipher()
        plain=x.decrypt(cipher,key1,key2)
        print "Decrypted using ",x.name," Cipher"
        print "The decrypted string is : ",plain
    else:
        print "Returning to Main Menu"

while True:
    print "Main Menu"
    print "1. Additive Cipher"
    print "2. Multiplicative Cipher"
    print "3. Affine Cipher"
    print "4. Exit"
    ch=input("Enter your choice: ")
    if ch==1:
        print
        Additive()
    elif ch==2:
        print
        Multiplicative()
    elif ch==3:
        print
        Affine()
    elif ch==4:
        break
    print
