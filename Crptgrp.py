# Implementation of crypyography concept using python

# Class for CrtpyoMachine for encoding and decoding purpose
class CryptoMachine():

    def __init__(self):
    	#Encoding pattern for message
        self.keys = "abN>c567yzABCG=.DIJ890 !kl-(mn}[opK?LM<{OPdefghij@#+]$%^EF;:,/H&*1234qrstUVWXuvwxQRSTYZ`)"
        #Decoding pattern for message
        self.values = self.keys[::-1]

    #	Method for encoder 
    def encoder(self):
        self.encryptDict = dict(zip(self.keys, self.values))

        self.message = input("Enter your secrete message : ")

        # Encrypting the given message 
        self.encodedMsg = "".join([self.encryptDict[letter] for letter in self.message])
        return self.encodedMsg


    #	Method for decoder 
    def decoder(self, secreteMsg):
        self.decryptDict = dict(zip(self.values, self.keys))

        self.secreteMsg = secreteMsg

        # Decrypting the given message 
        self.decodedMsg = "".join([self.decryptDict[letter] for letter in self.secreteMsg])
        return self.decodedMsg


# Main method
if __name__ == '__main__':

	# creating object of class
    coder = CryptoMachine()

    # Calling encoder method from cryptomachine class 
    msg = coder.encoder()

    # Display encoded message 
    print("\nEncoded message : " + msg)

    option = input("\nDo you want to decode the secrete msg (Y) or (N) : ")

    if option.lower() == 'y':

    	# calling decoded methond from cryptomachine class 
        print("\nDecoded Message : " + coder.decoder(msg))

        print("\nThanks for using the cryptography")

    else:

        print("\nThanks for using the cryptography")
