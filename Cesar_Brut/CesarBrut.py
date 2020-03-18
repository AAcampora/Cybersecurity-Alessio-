#this point onward is a copy of the code for the Cesar encryption
#cesar encripits by shift the letters by using a number key


#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
	result = ''

	# traverse text
	for i in range(len(text)):
		char = text[i]

		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result


#check the above function
text = "HACKED"
s = 4
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))

encryptText = (' ' + encrypt(text,s))
# this point is where i will try to decrypt the cesar key
#I will use the brute force method, as it is the easiest one and it will show why it is
#simple to decrypt this method

#we begin by making a new class

#we wrap this process inside a for loop in order to run through the various possibilites
#as we know, because Cesar uses letters, we will have 26 shifts

# we make a new param for the letters that we are gonna use to decyp
message = encryptText
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Now that we have the letters and the encrypted text, let's hack it
for key in range(len(Letters)):
    #get the range of letters to use
    translatedText = ''
    #for every symbol in the message, get me the letters, then shift them by a number, out put them, repeat
    for symbol in message:
        if symbol in Letters:
            num = Letters.find(symbol)
            num = num - key
            if num < 0:
                    num = num + len(Letters)
            translatedText = translatedText + Letters[num]
        else:
            translatedText = translatedText + symbol
    #print me the message, repeat
    print('Hacked key #%s: %s ' % (key, translatedText))

# as u can see, bruteforcing the key is possible, but it requires the hacker to screen the answers
#and decide which one of the outputs is the correct one
#at run of the code, in result number 4 of the brutforce, the messages should appear