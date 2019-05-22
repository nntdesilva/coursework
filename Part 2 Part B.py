while True:
    option=input("Enter 'e' to Encode the message\nEnter 'd' to Decode the message\nEnter 'q' to quit the program\nEnter your option: ")
    #for encoding the message
    if option == "e":
       
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

        print("The encoded message for your key is :",encodedMessage,"\n")

    #for decoding the message
    elif option == "d":
        alphabet="abcdefghijklmnopqrstuvwxyz" 
        key=int(input("Enter Key : ")) # Prompt the key
        message=input("Enter text : ") # Prompts the message
        decodedMessage="" 

        for character in message: # take each character in the message
            if character==" ":
                decodedMessage+=character
            elif character==character.upper():
                decodedMessage+=character
            elif alphabet.index(character)+key>25: # checks whether the addition of the index of the character and the key is greater than 25
                decodedMessage+=alphabet[alphabet.index(character)-key+25] 
            else:
                decodedMessage+=alphabet[alphabet.index(character)-key]
                
        print("The decoded message for your key is :",decodedMessage,"\n")    

    elif option == "q":
        print("Thank you for choosing and using our program...see you next time")
        break

    else:
        print("Attention! Please enter only 'e' or 'd' or 'q' as the option")
        

