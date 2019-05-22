alphabet="abcdefghijklmnopqrstuvwxyz"

while True:
    decodedMessage = input("Enter your Decoded message\n")
    plainText = input("Enter your plain text\n")

    fullEncodedMessage=""
    #using the bell ow loops the key is found
    for character in decodedMessage:
        if character == str(" "):
            continue
        else:
            indexDM = alphabet.index(character)
            break
    for character2 in plainText:
        if character == str(" "):
            continue
        else:
            indexPT = alphabet.index(character2)
            break
    key = indexDM - indexPT        

    #here we encode the message using the key
    for character in decodedMessage: # take each character in the message
        if character==" ":
            fullEncodedMessage+=character
        elif character==character.upper():
            fullEncodedMessage+=character
        elif alphabet.index(character)+key>25: # checks whether the addition of the index of the character and the key is greater than 25
            fullEncodedMessage+=alphabet[alphabet.index(character)-key+25] 
        else:
            fullEncodedMessage+=alphabet[alphabet.index(character)-key]
                
    print("The decoded message for your key is :",fullEncodedMessage,"\n")    

