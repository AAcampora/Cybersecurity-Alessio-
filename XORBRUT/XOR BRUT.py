# Python3 program to implement XOR - Encryption
#this is the snipped of code ive copied that was provided in the task
#Xor encrypting is the same concept, but instead of using letters it uses 256 bits for encryption as the key component.
#in order to decrypt, we are going to use the brut force again, like we did in cesar, to demonstrate how easy it is
#to decrypt, and why AES is vastly superior
# The same function is used to encrypt and
# decrypt
def encryptDecrypt(inpString):
    # Define XOR key
    # Any character value will work
    xorKey = 'P';

    # calculate length of input string
    length = len(inpString);

    # perform XOR operation of key
    # with every caracter in string
    for i in range(length):
        inpString = (inpString[:i] +
                     chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:]);
        print(inpString[i], end="");

    return inpString;


# Driver Code
if __name__ == '__main__':
    sampleString = "GeeksforGeeks";

    # Encrypt the string
    print("Encrypted String: ", end="");
    sampleString = encryptDecrypt(sampleString);
    cryptString = sampleString
    print("\n");

# in order to decrypt this message, we are going to wrap it inside a for loop
#and input every possible answer, then we are going to physically screenit, to
#see the correct answer

#iterate between every character from 0 to 256
for x in range(0, 256):
    #get the lenght of the key
    length = len(sampleString)
    #convert the current number in iteration to a key
    tryKey = str(chr(x))
    #do the xor algorithim with every single key in existence
    for i in range(length):
        cryptString = (cryptString[:i] +  chr(ord(cryptString[i]) ^ ord(tryKey)) + cryptString[i + 1:]);
        #print for each one and then screen (if you ctrl + f then search the code you can find the encrypted word between
        #iterations
        print('' + cryptString)


# This code is contributed by Princi Singh


