from Additive import AddCipher
while True:
    print "Main Menu"
    print "1. Encrypt"
    print "2. Decrypt"
    print "3. Exit"
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
    elif ch==3:
        break
    print
