def is_pangram(word):
    letters = []
    for char in word:
        if char.isalpha():
            letters.append(char.lower())
    letters = set(letters)
    if len(letters) == 26:
        return True
    return False
    

is_pangram("This is a word's")
