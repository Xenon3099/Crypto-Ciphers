class AffineCipher():
    def __init__(self):
        self.plaintext=""
        self.ciphertext=""
        self.key1=0
        self.key2=0
        self.name="Affine"
    def encrypt(self,plain,key1,key2):
        self.key1=key1
        self.key2=key2
        self.plaintext=plain
        self.ciphertext=""
        self.plaintext=self.plaintext.split()
        self.temp=""
        for i in self.plaintext:
            self.temp=self.temp+i.upper()
        self.plaintext=self.temp
        for i in self.plaintext:
            self.chara=chr((((ord(i)-65)*self.key1)%26)+65)
            self.ciphertext=self.ciphertext+self.chara
        self.plaintext=self.ciphertext
        self.ciphertext=""
        for i in self.plaintext:
            self.chara=chr((((ord(i)-65)+self.key2)%26)+65)
            self.ciphertext=self.ciphertext+self.chara
        return self.ciphertext
    def decrypt(self,cipher,key1,key2):
        self.key1=key1
        self.key2=key2
        self.plaintext=""
        self.ciphertext=cipher.upper()
        for i in self.ciphertext:
            self.chara=chr((((ord(i)-65)-self.key2)%26)+65)
            self.plaintext=self.plaintext+self.chara
        self.ciphertext=self.plaintext
        self.plaintext=""
        for i in self.ciphertext:
            self.chara=chr((((ord(i)-65)*self.modInverse(self.key1,26))%26)+65)
            self.plaintext=self.plaintext+self.chara
        return self.plaintext
    def modInverse(self,num,mod):
        num=num%mod
        for i in range(1,mod):
            if ((num*i)%mod==1):
                return i
        return 1
