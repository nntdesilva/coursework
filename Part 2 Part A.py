alphabet="abcdefghijklmnopqrstuvwxyz" 
key=int(input("Enter Key : ")) # Prompt the key
message=input("Enter text : ") # prompts the message
encodedMessage="" 

for character in message: # take each character in the message
    if character==" ":
        encodedMessage+=character
    elif character==character.upper():
        encodedMessage+=character
    elif alphabet.index(character)+key>25: # checks whether the addition of the index of the character and the key is greater than 25
        encodedMessage+=alphabet[alphabet.index(character)+key-25] 
    else:
        encodedMessage+=alphabet[alphabet.index(character)+key]
    

    
print("the encoded message for your key is :",encodedMessage)
