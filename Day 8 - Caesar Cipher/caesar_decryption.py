alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']

def encrypt(message, shift):
    encryptedMessage = ''
    for letter in message:
        if letter in alphabet:
            indexOfLetter = alphabet.index(letter)
            shiftedIndex = indexOfLetter + shift
            if shiftedIndex > 25:  # len(alphabet) - 1 = 25
                shiftedIndex = (shiftedIndex - 25) - 1  # -1 because of 0 index
            letter = alphabet[shiftedIndex]  # encrypted letter
        encryptedMessage += letter
    print(f"The encoded text is {encryptedMessage}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(message, shift):
    decrypedMessage = ''
    for letter in message:
        if letter in alphabet:
            indexOfDecryptedLetter = alphabet.index(letter) - shift
            letter = alphabet[indexOfDecryptedLetter]
        decrypedMessage += letter
    print(f'The decoded text is {decrypedMessage}')



#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print('Invalid Method!')
