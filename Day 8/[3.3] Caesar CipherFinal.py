alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numberList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def caesarCipher(direction, text, alphaShift, numShift=0):
    message = ''
    if alphaShift > 25 or numShift > 9:
        return 0
    for letter in text:
        if letter in alphabetList:
            if direction == 'decode':
                shiftedIndex = alphabetList.index(letter) - alphaShift
            else:
                shiftedIndex = alphabetList.index(letter) + alphaShift
            if shiftedIndex > 25:
                shiftedIndex = (shiftedIndex % 25) - 1
            letter = alphabetList[shiftedIndex]
        if letter in numberList:
            if direction == 'decode':
                shiftedIndex = numberList.index(letter) - numShift
            else:
                shiftedIndex = numberList.index(letter) + numShift
            if shiftedIndex > 9:
                shiftedIndex = (shiftedIndex % 9) - 1
            letter = numberList[shiftedIndex]
        message += letter
    return message





direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
alphaShift = int(input("Type the shift for alphabets [1-25]:\n"))
numShift = int(input("Type the shift for numbers [1-9]:\n"))

outputText = caesarCipher(direction, text, alphaShift, numShift)
print(f'{direction}: {outputText}')

