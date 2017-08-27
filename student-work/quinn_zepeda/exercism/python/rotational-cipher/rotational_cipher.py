
# a = 97
# z = 122
# A 65
# Z 96

def rotate(word, amount):
    final = ""
    for char in word:
        if not char.isalpha():
            stayInAlphabet = ord(char)
        if char.isalpha():
            if ord(char) <= 96:
                stayInAlphabet = ord(char) + amount
                if stayInAlphabet > ord('Z'):
                    stayInAlphabet -= 26
            elif ord(char) > 96 and ord(char) < 123:
                stayInAlphabet = ord(char) + amount
                if stayInAlphabet > ord('z'):
                    stayInAlphabet -= 26
        finalLetter = chr(stayInAlphabet)
        final += finalLetter
    return final
